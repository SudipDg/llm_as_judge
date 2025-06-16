# main.py

from app.document_loader import load_and_split_document
from app.evaluator import evaluate_document_sections
import json

if __name__ == "__main__":
    print("📄 Loading document...")
    file_path = "data/FDD_PR_Approval_Report.docx"
    sections = load_and_split_document(file_path)

    print("🚀 Evaluating document sections...\n")
    results = evaluate_document_sections(sections)

    # Save results for review
    with open("results/reviewed_outputs.json", "w") as f:
        json.dump(results, f, indent=2)

    # Print to console
    for result in results:
        print("\n" + "="*40)
        print(f"📌 Section: {result.get('section', 'N/A')}")
        if "error" in result:
            print(f"❌ Error: {result['error']}")
        else:
            for metric, detail in result["ratings"].items():
                print(f"- {metric.capitalize()}: {detail['score']} ⭐")
                print(f"  Feedback: {detail['feedback']}")
