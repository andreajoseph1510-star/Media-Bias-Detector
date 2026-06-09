import streamlit as st
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(
    page_title="Media Bias Detector",
    page_icon="📰",
    layout="wide",
)
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
st.write("API Key Loaded:", GEMINI_API_KEY is not None)
# --- Custom CSS for Black-Green Neon Theme ---
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #00FF00;
    }
    .stTextArea textarea {
        background-color: #111111;
        color: #00FF00;
        border: 1px solid #00FF00;
    }
    .stButton>button {
        background-color: #00FF00;
        color: #000000;
        border-radius: 8px;
        font-weight: bold;
    }
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #00FF00 !important;
    }
    .reportview-container .markdown-text-container {
        color: #00FF00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>📰 Media Bias Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze media text for bias, reasoning, and neutral rewriting</p>", unsafe_allow_html=True)

# --- Input Section ---
st.subheader("Paste or Upload Media Content")
user_input = st.text_area("Enter article, post, or snippet:", height=200)

uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])

if uploaded_file is not None:
    user_input = uploaded_file.read().decode("utf-8")

# --- Action Button ---
if st.button("Analyze Bias"):
    if user_input.strip() == "":
        st.warning("⚠️ Please provide some text to analyze.")

    else:
        with st.spinner("Analyzing article..."):

            prompt = f"""
            Analyze this article.

            Return ONLY in this format:

            Bias Score: <0-100>

            Sentiment:
            <Positive/Negative/Neutral>

            Reasoning:
            <Explain the bias>

            Neutral Rewrite:
            <Rewrite objectively>

            Article:
            {user_input}
            """

            response = model.generate_content(prompt)

            st.success("✅ Analysis Complete")

            st.markdown("## Analysis Result")
            st.write(response.text)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
#st.markdown("<p style='text-align: center;'>Made with 💚 Neon & Streamlit</p>", unsafe_allow_html=True)
if st.button("Test Gemini"):
    response = model.generate_content(
        "Explain media bias in one sentence."
    )

    st.success("Gemini Connected!")
    st.write(response.text)