# app/evaluator.py

from typing import Dict, List
import time
from app.agents import get_all_agents
from openai import OpenAI
from utils.utils import get_openai_api_key

client = OpenAI(api_key=get_openai_api_key())
agents = get_all_agents()

def run_agent_review(agent, section_title: str, section_text: str) -> Dict:
    """
    Run a single agent on a document section.
    """
    prompt = f"""
You are the {agent.role}. Review the following section:

Section Title: {section_title}
Content:
\"\"\"
{section_text}
\"\"\"

Return your review as JSON:
{{
  "parameter": "{agent.role}",
  "score": X,  // 1 to 10
  "feedback": "Your specific feedback here"
}}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        result = response.choices[0].message.content.strip()
        return eval(result)

    except Exception as e:
        return {
            "parameter": agent.role,
            "score": 0,
            "feedback": f"Error from agent: {str(e)}"
        }


def evaluate_section_with_agents(section_title: str, section_text: str) -> Dict:
    """
    Evaluate a section using all agents and return combined scores and feedback.
    """
    section_result = {
        "section": section_title,
        "ratings": {}
    }

    for agent in agents:
        print(f"🤖 {agent.role} reviewing '{section_title}'")
        review = run_agent_review(agent, section_title, section_text)

        section_result["ratings"][review["parameter"].lower()] = {
            "score": review["score"],
            "feedback": review["feedback"]
        }
        time.sleep(1.5)

    return section_result


def evaluate_document_sections(sections: Dict[str, str]) -> List[Dict]:
    """
    Evaluate all document sections and return their scores and feedback.
    """
    results = []
    for title, content in sections.items():
        print(f"📄 Evaluating Section: {title}")
        result = evaluate_section_with_agents(title, content)
        results.append(result)
    return results
