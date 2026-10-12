# PRiVERA

**PRIVacy-preserving, Explainable Retrieval Assistant**

PRiVERA explores query-specific context selection for retrieval-based assistants: select information relevant to a query, explain selection decisions, and withhold unrelated information where appropriate.

> **Project status:** Early-stage baseline implementation. This is not yet a validated privacy mechanism or a completed research system.

## Current implementation

- Fictional personal-profile records stored as JSON.
- TF-IDF candidate retrieval.
- Transparent, rule-based necessity filtering.
- Streamlit interface showing selected and withheld records with explanations.

## Quick start

Python 3.10+ is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually `http://localhost:8501`).

## Example queries

- `What programming skills does the user have?`
- `What projects has the user built?`
- `What is the user's CGPA?`
- `What is the user's phone number?`

## Limitations

- TF-IDF is lexical retrieval, not a neural embedding model.
- Necessity decisions are hand-written heuristics, not a trained model.
- Scores are heuristic indicators, not calibrated probabilities.
- Responses are assembled from selected records; no LLM is connected.
- No formal privacy guarantee or validated empirical result is claimed.
- Keep demo data fictional in public examples.

## Research directions

1. Define a reproducible query-specific disclosure policy.
2. Compare the baseline with alternative selection methods.
3. Evaluate answer sufficiency, information disclosure, retrieval quality, and explainability using a documented test set.
4. Add automated tests and reproducible experiments.
5. Review threat models and data handling before introducing real personal data.

## Repository structure

```text
PRiVERA/
├── app.py
├── data/profile.json
├── src/engine.py
├── src/__init__.py
├── requirements.txt
└── README.md
```

Record experiments honestly, including limitations and failures. Do not commit passwords, API keys, access tokens, private data, or personal institutional documents.

## License

No license has been added yet. Confirm university requirements before choosing one.
