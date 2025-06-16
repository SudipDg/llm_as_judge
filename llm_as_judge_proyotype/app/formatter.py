# app/formatter.py

import guidance
from openai import OpenAI as OpenAIClient
from utils.utils import get_openai_api_key

# Set LLM globally for guidance
api_key = get_openai_api_key()
guidance.llm = OpenAIClient(api_key=api_key)

# ✅ Define the template as a function and attach it with `@guidance`
@guidance
def review_template(section_title, section_content, parameter):
    """
You are an expert documentation reviewer for enterprise documents.

Section Title: {{section_title}}
Section Content:
---
{{section_content}}
---

You are evaluating the section for its {{parameter}}.

Return your evaluation strictly in this JSON format:
{
  "parameter": "{{parameter}}",
  "score": {{gen "score"}},
  "feedback": "{{gen "feedback"}}"
}
    """
    pass

def run_guided_review(section_title: str, section_content: str, parameter: str) -> dict:
    try:
        output = review_template(
            section_title=section_title,
            section_content=section_content,
            parameter=parameter
        )
        return eval(str(output))
    except Exception as e:
        return {
            "parameter": parameter,
            "score": 0,
            "feedback": f"❌ Error from Guidance: {str(e)}"
        }
