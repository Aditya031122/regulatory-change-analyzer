# Regulatory Change Analyzer

A tool that helps QA and regulatory teams quickly spot changes between document versions and understand their impact. Built for the zipp.ai intern assessment.

## What it does

- Compares two text files and finds what's been added, deleted, or modified
- Uses a local LLM (Gemma 2B) to analyze each change and categorize it
- Shows results in a clean web interface

## Setup

1. **Install Ollama** from https://ollama.ai
2. **Pull the model**: `ollama pull gemma:2b`
3. **Install dependencies**: `pip install streamlit requests`
4. **Run**: `streamlit run app.py`

## Usage

1. Upload "before" and "after" text files
2. Click "Analyze Changes"
3. Review categorized results (new requirements, clarifications, etc.)

## How it works

- **Change Detection**: Uses `difflib.ndiff` to compare files line by line
- **LLM Analysis**: Sends changes to Gemma 2B for categorization (new requirement, clarification, etc.)
- **Frontend**: Simple Streamlit interface with file uploads and expandable results

---


| Component      | Tech Used              |
|----------------|------------------------|
| Frontend       | Streamlit              |
| Backend        | Python                 |
| LLM            | [Gemma:2b](https://ollama.com/library/gemma) via Ollama |
| Diff Engine    | Python’s `difflib`     |

---


Built for zipp.ai's intern assessment on AI solutions for regulated industries.

