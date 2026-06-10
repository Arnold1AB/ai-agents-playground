from dotenv import load_dotenv
import os

import streamlit as st

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()

model = OpenAIChatModel(
    "openai/gpt-oss-120b",
    provider=OpenAIProvider(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
    ),
)

agent = Agent(
    model=model,
    system_prompt="""
    You are a friendly greeting assistant.

    Help users greet people in different languages
    and communication styles.
    """,
)

st.set_page_config(page_title="Greeting Agent")

st.title("🌍 Greeting Agent")
st.write("Ask me how to greet people in any language.")

user_input = st.text_input(
    "Enter your question",
    placeholder="How do I greet someone professionally in French?"
)

if st.button("Ask") and user_input:
    with st.spinner("Thinking..."):
        result = agent.run_sync(user_input)

    st.markdown(result.output)