# CrewAI Integration Scaffold

This folder contains a CrewAI orchestration layer for the insurance claim workflow.

## Included structure

- crewai/
  - config/
    - crew.yaml
    - agents.yaml
    - tasks.yaml
  - agents/
    - crew.py
    - base_agent.py
  - tools/
    - backend_adapter.py
    - cv_tool.py
    - nlp_tool.py
    - rag_tool.py
    - fraud_tool.py
    - decision_tool.py

## Notes

- Existing backend services remain unchanged.
- CrewAI is used only as an orchestration layer.
- No business logic has been duplicated.
- The integration currently imports the installed CrewAI runtime when present and remains import-safe in environments without that runtime.
