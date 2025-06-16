# 🤖 LLM-as-a-Judge Prototype

This prototype is a multi-agent LLM-powered document evaluator designed to review structured business documents (like Functional Design Documents). It uses OpenAI’s GPT-4 and CrewAI agents to assess clarity, completeness, accuracy, and consistency.

---

## 🚀 Features

- 📤 Upload `.docx` documents via Streamlit
- 📚 Automatically split sections (e.g., Introduction, Business Requirements)
- 🧠 Evaluate each section using multiple AI agents
- 🧾 Receive a score and actionable feedback per section and metric
- 📥 Download results as a CSV file

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) for the UI
- [OpenAI](https://openai.com/) for LLM-based evaluation
- [CrewAI](https://github.com/joaomdmoura/crewAI) for agent task routing
- `python-docx`, `tqdm`, `dotenv` for file handling and environment setup

---

## 📁 Project Structure

```
llm_as_judge_prototype/
├── app/                # App logic
├── data/               # Uploaded docs
├── results/            # Evaluation output
├── utils/              # API key loader
├── app.py              # Streamlit UI
├── main.py             # CLI test runner
├── .env                # Your OpenAI key
├── requirements.txt
└── README.md
```

---

## 📥 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/yourname/llm-as-a-judge.git
   cd llm_as_judge_prototype
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your `.env` file:
   ```
   OPENAI_API_KEY=sk-xxxxxxx
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Sample Document

Use 'data/FDD_Vendor_Invoice_Enhancement.docx' as a test case to see multi-agent evaluation in action.

---

## 👥 Authors

Built by:
- Sudip Dasgupta
- Himanshu Shiv Shankar

---

## 🛡️ License

This project is licensed for research and internal prototyping only.
