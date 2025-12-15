# agent.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class GrammarAgent:
    def __init__(self):
        print("Loading grammar correction model (first time may take a few minutes)...")

        self.model_name = "vennify/t5-base-grammar-correction"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

        print("Model loaded successfully.\n")

    def post_process(self, text: str) -> str:
        """
        Post-processing rules to stabilize model output
        """

        # Fix common spacing mistakes
        fixes = {
            "some where": "somewhere",
            "Some where": "Somewhere",
            "every thing": "everything",
            "Every thing": "Everything",
            "any thing": "anything",
            "Any thing": "Anything",
        }

        for wrong, correct in fixes.items():
            text = text.replace(wrong, correct)

        # Split text into sentences
        sentences = [s.strip() for s in text.split(".") if s.strip()]

        # Remove duplicate sentences while preserving order
        unique_sentences = []
        for sentence in sentences:
            if sentence not in unique_sentences:
                unique_sentences.append(sentence)

        # Capitalize first letter of each sentence
        final_sentences = []
        for s in unique_sentences:
            if s:
                final_sentences.append(s[0].upper() + s[1:])

        # Join sentences properly
        return ". ".join(final_sentences) + "."

    def correct(self, sentence: str) -> str:
        """
        Correct grammar of the input sentence
        """
        if not sentence.strip():
            return "Please enter a valid sentence."

        inputs = self.tokenizer.encode(
            sentence,
            return_tensors="pt",
            truncation=True,
            max_length=128
        )

        outputs = self.model.generate(
            inputs,
            max_length=128,
            num_beams=5,
            early_stopping=True
        )

        corrected_text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return self.post_process(corrected_text)
