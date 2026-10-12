import streamlit as st

from src.engine import run_privera

st.set_page_config(page_title="PRiVERA", page_icon="🛡️", layout="wide")
st.title("PRiVERA")
st.caption("PRIVacy-preserving, Explainable Retrieval Assistant")
st.info(
    "Early-stage baseline: fictional profile data, TF-IDF retrieval, and "
    "rule-based necessity filtering. This is not a validated privacy guarantee."
)

query = st.text_input(
    "Ask a question about the demo profile",
    placeholder="What programming skills does the user have?",
)

if st.button("Run PRiVERA", type="primary"):
    if not query.strip():
        st.warning("Enter a question first.")
    else:
        result = run_privera(query)
        st.subheader("Baseline response")
        st.write(result["answer"])

        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Retrieved candidates", len(result["candidates"]))
        col_b.metric("Selected for disclosure", len(result["disclosed"]))
        col_c.metric("Withheld", len(result["withheld"]))

        left, right = st.columns(2)
        with left:
            st.subheader("Selected context")
            if not result["disclosed"]:
                st.write("No information selected.")
            for item in result["disclosed"]:
                with st.container(border=True):
                    st.write(item["content"])
                    st.caption(item["decision_reason"])
                    st.caption(f"Heuristic indicator: {item['necessity_score']:.2f}")

        with right:
            st.subheader("Withheld context")
            if not result["withheld"]:
                st.write("No retrieved items withheld.")
            for item in result["withheld"]:
                with st.container(border=True):
                    st.write(item["content"])
                    st.caption(item["decision_reason"])
                    st.caption(f"Heuristic indicator: {item['necessity_score']:.2f}")

        with st.expander("Inspect retrieval candidates"):
            for item in result["candidates"]:
                st.write(
                    f"{item['id']} | {item['content']} | "
                    f"TF-IDF score: {item['retrieval_score']:.3f}"
                )

st.divider()
st.caption(
    "Demo data is fictional. Necessity indicators are heuristic, not probabilities. "
    "No LLM is connected."
)
