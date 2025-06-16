# app.py

import streamlit as st
import os
import json
import time
from app.document_loader import load_and_split_document
from app.evaluator import evaluate_document_sections

st.set_page_config(page_title="LLM-as-a-Judge", layout="wide")
st.title("🤖 LLM-as-a-Judge: Automated Document Reviewer")
st.markdown(
    "<p style='text-align: right; font-size: 15px;'>Developed by Sudip Dasgupta and Himanshu Shiv Shankar</p>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📤 Upload your business document (.docx)", type=["docx"])

if uploaded_file:
    st.success("✅ File uploaded!")

    # Save uploaded file with unique timestamp to avoid permission issues
    timestamp = int(time.time())
    base_name = os.path.splitext(uploaded_file.name)[0]
    safe_name = f"{base_name}_{timestamp}.docx"
    save_path = os.path.join("data", safe_name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info(f"📄 File saved as: {save_path}")

    if st.button("🔍 Run Evaluation"):
        with st.spinner("Running evaluation..."):
            sections = load_and_split_document(save_path)
            results = evaluate_document_sections(sections)

            # Save JSON for traceability
            with open("results/reviewed_outputs.json", "w") as out_file:
                json.dump(results, out_file, indent=2)

            # Flatten structure for display
            display_rows = []
            for section in results:
                section_name = section.get("section", "N/A")
                ratings = section.get("ratings", {})
                for param, data in ratings.items():
                    display_rows.append({
                        "Section": section_name,
                        "Parameter": param.capitalize(),
                        "Score (out of 10)": data.get("score", ""),
                        "Feedback": data.get("feedback", "")
                    })

            st.success("✅ Evaluation completed!")
            st.subheader("📊 Multi-Agent Document Review")
            st.dataframe(display_rows, use_container_width=True)

# Footer

