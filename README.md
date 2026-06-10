# AI Agents Playground

A public repository documenting my journey building AI-powered agents with Python, Google's Agent Development Kit (ADK), Groq, and LiteLLM.

This repository contains hands-on examples covering everything from simple conversational agents to advanced multi-agent systems with memory, tools, workflows, and persistent storage.

---

## Overview

The goal of this project is to learn and demonstrate modern AI agent development using:

* Python
* Google Agent Development Kit (ADK)
* Groq LLMs
* LiteLLM
* Pydantic
* Environment Variables
* Multi-Agent Architectures

Rather than relying on Google Cloud billing requirements, this project uses Groq's fast inference API to power AI agents while keeping costs low and development accessible.

---

## Project Structure

```text
ai-agents-playground/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── 01-basic-agent/
│   └── greeting_agent/
│
├── 02-tool-agent/
│
├── 03-litellm-agent/
│
├── 04-structured-output/
│
├── 05-sessions-state/
│
├── 06-persistent-storage/
│
├── 07-multi-agent/
│
├── 08-stateful-multi-agent/
│
├── 09-callbacks/
│
├── 10-sequential-agent/
│
├── 11-parallel-agent/
│
├── 12-loop-agent/
│
└── notes/
```

Each folder focuses on a specific ADK concept and builds upon previous lessons.

---

## Technologies Used

### Python

The primary programming language used for building all agents and workflows.

### Google ADK

Google's Agent Development Kit provides the framework for building, orchestrating, and managing LLM-powered agents.

### Groq

Groq provides ultra-fast inference for open-source language models.

This repository uses Groq as the primary LLM provider instead of Gemini.

### LiteLLM

LiteLLM acts as a provider abstraction layer, making it easy to switch between:

* Groq
* OpenAI
* Gemini
* Anthropic
* Ollama

without changing core application logic.

---

## Why Groq Instead of Gemini?

Many Google ADK tutorials use Gemini models through Google Cloud.

While powerful, Google Cloud often requires billing setup and payment verification before production usage.

Groq offers:

* Free development tier
* Fast response times
* Easy API setup
* Support for leading open-source models

This makes Groq an excellent option for learning AI agent development.

---

## Environment Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-agents-playground.git

cd ai-agents-playground
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install google-adk
pip install litellm
pip install groq
pip install python-dotenv
```

---

## Getting a Groq API Key

1. Create an account at Groq Console
2. Generate a new API Key
3. Copy the key

---

## Configure Environment Variables

Create a `.env` file inside your agent folder:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
```

Never commit API keys to GitHub.

---

## Example Agent Structure

```text
greeting_agent/
│
├── __init__.py
├── agent.py
└── .env
```

---

### **init**.py

```python
from . import agent
```

---

### agent.py

```python
from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="greeting_agent",
    model="groq/llama3-70b-8192",
    instruction="""
    You are a helpful assistant that specializes in greetings.

    Help users greet people in different languages.
    """
)
```

---

## Running Agents

Navigate to the parent directory containing the agent folder.

Launch the ADK web interface:

```bash
adk web
```

Default URL:

```text
http://localhost:8000
```

Select your agent and begin interacting.

---

## Learning Roadmap

### Phase 1 — Foundations

* Basic Agent
* Prompt Engineering
* Agent Instructions
* Agent Identity

### Phase 2 — Agent Tools

* Custom Tools
* External APIs
* Data Retrieval

### Phase 3 — Structured Systems

* Structured Outputs
* Pydantic Schemas
* Validation

### Phase 4 — Memory

* Sessions
* State Management
* Persistent Storage

### Phase 5 — Multi-Agent Systems

* Specialized Agents
* Agent Delegation
* Agent Orchestration

### Phase 6 — Advanced Workflows

* Sequential Agents
* Parallel Agents
* Loop Agents
* Event Callbacks

---

## Git Workflow

Commit changes regularly:

```bash
git add .

git commit -m "Build basic greeting agent"

git push origin main
```

Example milestones:

```bash
git commit -m "Complete tool agent example"

git commit -m "Implement structured outputs"

git commit -m "Add multi-agent workflow"
```

---

## Security

Never commit:

```text
.env
.env.local
*.key
```

Ensure `.gitignore` contains:

```text
.env
.venv/
__pycache__/
```

---

## Future Improvements

* Retrieval Augmented Generation (RAG)
* Vector Databases
* Agent Memory Systems
* Autonomous Agent Workflows
* AI Product Integrations
* Production Deployment

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute the code while retaining attribution.

---

## Author

Abraham Arnold

Learning in public and building AI agents one project at a time.
