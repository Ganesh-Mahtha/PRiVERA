# Project status

## Current implementation
- Streamlit interface for query entry and inspection.
- TF-IDF lexical candidate retrieval.
- Rule-based necessity baseline.
- Fictional profile records for demonstration.
- Selected/withheld context views with human-readable rule explanations.

## Explicit limitations
- Retrieval is lexical TF-IDF.
- Necessity decisions are heuristic rules.
- Heuristic values are not calibrated probabilities.
- No LLM is connected.
- No validated experimental results or formal privacy guarantees yet.

## Suggested next milestones
1. Confirm scope and threat model with the project guide.
2. Define query categories and information units available for disclosure.
3. Create a small documented test set using synthetic records.
4. Add automated tests for retrieval and disclosure decisions.
5. Define evaluation measures before running experiments.
6. Compare the current baseline with at least one alternative.
7. Record results reproducibly and report limitations honestly.
8. Review data handling before introducing real personal information.
