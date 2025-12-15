# main.py
from agent import GrammarAgent

def main():
    agent = GrammarAgent()
    print("Grammar Correction Agent is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter sentence: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        corrected = agent.correct(user_input)
        print("Corrected:", corrected, "\n")

if __name__ == "__main__":
    main()
