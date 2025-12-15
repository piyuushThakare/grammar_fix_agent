import streamlit as st
from agent import GrammarAgent

st.set_page_config(
    page_title="Grammar Correction Agent",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Grammar Correction Agent")
st.write("Correct your English sentences using AI")

@st.cache_resource
def load_agent():
    return GrammarAgent()

agent = load_agent()

user_input = st.text_area(
    "Enter your sentence:",
    height=150,
    placeholder="Type your sentence here..."
)

if st.button("Correct Grammar"):
    if user_input.strip():
        with st.spinner("Correcting grammar..."):
            result = agent.correct(user_input)

        st.success("Corrected Sentence:")
        st.write(result)
    else:
        st.warning("Please enter a sentence.")
