import streamlit as st

st.set_page_config(page_title="AI Media Bias Detector", layout="wide")

page_style = """
<style>
body {
    background-color: #020202;
    color: #e8f5e9;
}
section.main {
    background: linear-gradient(180deg, #040404 0%, #08120c 100%);
    padding: 1rem 2rem 2rem 2rem;
    border-radius: 26px;
    box-shadow: 0 20px 60px rgba(0, 255, 128, 0.12);
}
.stApp {
    background-color: #020202;
}
.css-1d391kg {
    background-color: #050505;
}
.stButton>button {
    background-color: #00ff6a;
    color: #071e10;
    border: none;
    border-radius: 100px;
    padding: 0.85rem 2rem;
    font-weight: 700;
    box-shadow: 0 10px 30px rgba(0, 255, 106, 0.24);
}
.stButton>button:hover {
    background-color: #1bff83;
}
.stTextArea>div>div>textarea {
    background-color: #081613;
    color: #e8f5e9;
    border: 1px solid #0d2d1f;
}
.stTextArea>label {
    color: #b7f2c7;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    color: #c7ffc7;
}
.stMetricValue {
    color: #ffffff;
}
.stMetricLabel {
    color: #a6f7b3;
}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

st.markdown("## AI Media Bias Detector")
st.markdown("Analyze news articles and media copy for persuasive or unbalanced language with a modern bias insight dashboard.")

with st.container():
    left, right = st.columns([2, 1])

    with left:
        article_text = st.text_area(
            "Paste article text here",
            height=320,
            placeholder="Paste the full article content you want to evaluate for bias and tone..."
        )

        analyze_clicked = st.button("Analyze")

    with right:
        st.markdown("### Quick Notes")
        st.markdown(
            "- Use this tool to preview bias signals in text.\n"
            "- Results shown are placeholder data for now.\n"
            "- The design is built for a dark green, professional look."
        )

if analyze_clicked:
    st.write("---")
    st.markdown("### Analysis Results")

    score_col, emotion_col, category_col = st.columns(3)
    score_col.metric("Bias Score", "72%", delta="Moderate")
    emotion_col.metric("Emotional Language", "Moderate", delta="Sensational")
    category_col.metric("Bias Categories", "Political, Sensational, Confirmation")

    st.markdown("#### Neutral Rewrite")
    st.success(
        "The article highlights key events and viewpoints while replacing charged or partisan phrasing with objective, fact-based language."
    )

    st.markdown("#### Summary")
    st.info(
        "This article contains a noticeable bias toward one perspective, using emotionally loaded terms and confirming language."
        " A neutral rewrite refocuses the narrative on events and facts without opinionated framing."
    )

    st.markdown("---")
    st.markdown("#### Notes")
    st.write(
        "Placeholder results are being displayed for design validation. Once connected to an AI analysis engine, these values will reflect real bias scoring, emotional tone and category detection."
    )
