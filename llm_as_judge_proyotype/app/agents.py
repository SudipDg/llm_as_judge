# app/agents.py

from crewai import Agent
from utils.utils import get_openai_api_key
from openai import OpenAI

# Initialize OpenAI client
openai_client = OpenAI(api_key=get_openai_api_key())

# Agent 1: Template Compliance
template_compliance_agent = Agent(
    role="Template Compliance Checker",
    goal="Ensure the section follows the expected business template structure",
    backstory="Expert in corporate documentation and regulatory formatting standards.",
    verbose=True,
    allow_delegation=False,
    llm=openai_client
)

# Agent 2: Accuracy
accuracy_checker_agent = Agent(
    role="Factual Accuracy Reviewer",
    goal="Identify any technical inaccuracies or inconsistent facts in the section",
    backstory="Senior domain SME who understands the context and data in enterprise systems.",
    verbose=True,
    allow_delegation=False,
    llm=openai_client
)

# Agent 3: Completeness
completeness_validator_agent = Agent(
    role="Completeness Validator",
    goal="Check whether all important business aspects are covered in the section",
    backstory="A business analyst who knows what decision-makers look for in documentation.",
    verbose=True,
    allow_delegation=False,
    llm=openai_client
)

# Agent 4: Clarity
clarity_reviewer_agent = Agent(
    role="Clarity Reviewer",
    goal="Ensure the section is clear, professional, and uses correct business language",
    backstory="Experienced enterprise editor who ensures clarity in official documentation.",
    verbose=True,
    allow_delegation=False,
    llm=openai_client
)


# A helper function to return the list of agents (for orchestration)
def get_all_agents():
    return [
        template_compliance_agent,
        accuracy_checker_agent,
        completeness_validator_agent,
        clarity_reviewer_agent
    ]
