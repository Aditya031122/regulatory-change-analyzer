# 📄 Regulatory Change Analyzer

An AI-powered tool that compares two versions of regulatory documents and identifies **added**, **deleted**, and **modified** sections. It uses a local Large Language Model (LLM) to summarize and categorize the impact of each change.

---

## 🚀 Features

- 📤 Upload two text documents (Old vs New)
- 🔍 Automatically detect:
  - ✅ Added sections
  - ❌ Deleted sections
  - ✏️ Modified sections
- 🤖 AI analysis using **Gemma 2B LLM** via **Ollama**
  - Generates a one-line summary
  - Categorizes the change as:
    - New Requirement
    - Clarification of Existing Requirement
    - Deletion of Requirement
    - Minor Edit
- 📋 Clean Streamlit interface with structured layout and expanders

---

## 🛠️ Tech Stack

| Component      | Tech Used              |
|----------------|------------------------|
| Frontend       | Streamlit              |
| Backend        | Python                 |
| LLM            | [Gemma:2b](https://ollama.com/library/gemma) via Ollama |
| Diff Engine    | Python’s `difflib`     |

---



