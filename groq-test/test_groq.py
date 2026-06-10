from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
import os

load_dotenv()

model = OpenAIModel(
    model_name="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

agent = Agent(
    model=model,
    system_prompt="You are a friendly greeting assistant."
)

result = agent.run_sync(
    "How do I greet someone professionally in French?"
)

print(result.output)