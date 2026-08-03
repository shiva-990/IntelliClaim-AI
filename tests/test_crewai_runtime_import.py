import importlib


def test_crewai_agent_and_crew_modules_import():
    base_agent = importlib.import_module("crewai.agents.base_agent")
    crew_module = importlib.import_module("crewai.agents.crew")

    assert base_agent.CrewAgentFactory is not None
    assert crew_module.InsuranceClaimCrew is not None
