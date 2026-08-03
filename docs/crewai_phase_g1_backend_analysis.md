# Phase G1 — Backend Analysis for CrewAI Integration

## Objective
Map the current backend so CrewAI can orchestrate existing services without rewriting or duplicating business logic.

## Current architecture summary

The backend is already organized as a layered AI processing system:

- FastAPI entry point: main.py
- Versioned API composition: api/v1.py
- Domain routes: api/routes/
- Service orchestration: services/claim_processing_service.py
- Specialized modules:
  - Computer vision: cv/services/
  - NLP: nlp/services/
  - RAG: rag/services/
  - Persistence: database/

## Existing execution flow

The current claim-processing path is:

1. Upload images through the upload API.
2. Run CV detection through DetectionService.
3. Run NLP extraction through NLPService.
4. Run policy verification through RAGService.
5. Generate final decision through DecisionService.
6. Persist results via database CRUD modules.

## Reusable backend services

These services are the authoritative implementation layer and must remain the source of truth:

- DetectionService
  - detect_claim(claim_id)
  - save_results(db, claim_id, predictions)

- NLPService
  - analyze_claim(db, claim_id)

- RAGService
  - verify_policy(db, claim_id)

- DecisionService
  - process_claim(db, claim_id)

- ClaimProcessingService
  - process_claim(db, claim_id)
  - This is the current composite orchestrator.

## Integration boundary

CrewAI should not own:

- database persistence
- validation rules
- claim business logic
- model execution details

CrewAI should only orchestrate existing services through thin adapters.

## Recommended design rule

Use CrewAI as a coordination layer around the existing backend, not as a replacement for it.

### In practice
- CrewAI will receive a claim_id and db context.
- CrewAI will delegate work to existing services.
- CrewAI will return a structured result that is consistent with the current backend contract.

## Architectural constraints

These rules are non-negotiable:

- Do not rewrite existing backend modules.
- Do not duplicate current business logic.
- Reuse DetectionService, NLPService, RAGService, and DecisionService.
- Keep persistence and state transitions in the backend.

## Phase G1 outcome

Backend analysis is complete. The next phase will define the CrewAI folder structure without touching the existing backend implementation.
