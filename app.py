import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- Page Config ---
st.set_page_config(
    page_title="Reality Lens AI",
    page_icon="🌎",
    layout="wide",
)

# --- Load Environment ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Custom CSS for Black-Green + Neon Blue Theme ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

    body {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Press Start 2P', cursive;
    }

    .stTextArea textarea {
        background-color: #111111;
        color: #00FF00;
        border: 2px solid #00FF00;
        font-family: 'Press Start 2P', cursive;
    }

    /* --- Neon Blue Section Headers --- */
    .neon-header {
        font-family: 'Press Start 2P', cursive;   /* keep pixel font for headings */
        color: #00bfff;                           /* lighter neon blue */
        text-shadow: 0 0 1px #00bfff, 0 0 2px #00bfff; /* reduced glow */
        font-size: 16px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    /* --- Light glow only for main title --- */
    .main-title {
        font-family: 'Press Start 2P', cursive;   /* keep pixel font */
        color: #00ccff;                           /* bright cyan */
        text-shadow: 0 0 4px #00bbff, 0 0 8px #00bbff; /* gentle glow */
        font-size: 28px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* --- Normal readable content --- */
    .analysis-output, .stTextArea textarea, .stMarkdown p {
        font-family: 'Inter', sans-serif;        /* clean modern font */
        font-size: 14px;
        line-height: 1.6;
        color: #00cc00;
    }

    /* --- Improve readability for analysis output --- */
    .analysis-output {
        background-color: #0a0a0a;
        border: 1px solid #00ff00;
        border-radius: 6px;
        padding: 15px;
        margin-top: 15px;
    }


    .stButton>button {
        background-color: #00FF00;
        color: #000000;
        border-radius: 8px;
        font-weight: bold;
        font-family: 'Press Start 2P', cursive;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #00cc00;
        transform: scale(1.05);
    }

    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #00FF00 !important;
        font-family: 'Press Start 2P', cursive;
    }
    .stAlert {
        border: 1px solid #00ff00;
        border-radius: 6px;
        background-color: #0a0a0a;
        color: #00ff00;
    }

    .robot {
        position: relative;
        animation: moveRobot 6s infinite alternate ease-in-out;
        width: 120px;
        margin: auto;
    }

    @keyframes moveRobot {
        0% { transform: translateX(-60px); }
        100% { transform: translateX(60px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown(
    """
    <div style='text-align:center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/4712/4712100.png' class='robot'>
        <h1 class='main-title'>🌎 Reality Lens AI</h1>
        <p>Decode Bias. Discover Truth.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Input Section ---
st.markdown("<div class='neon-header'>Paste or Upload Media Content</div>", unsafe_allow_html=True)
user_input = st.text_area("Enter article, post, or snippet:", height=200)

uploaded_file = st.file_uploader("Or upload a text file", type=["txt"])
if uploaded_file is not None:
    user_input = uploaded_file.read().decode("utf-8")

# --- Perspective Selection ---
st.markdown("<div class='neon-header'>Perspective Comparison</div>", unsafe_allow_html=True)
perspective = st.selectbox(
    "Choose a perspective",
    ["Neutral", "Progressive", "Conservative", "Optimistic", "Pessimistic"]
)

# --- Analyze Button ---
if st.button("Analyze Bias"):
    if user_input.strip() == "":
        st.warning("⚠️ Please provide some text to analyze.")
    else:
        with st.spinner("Analyzing article..."):
            prompt = f"""
            Analyze the following news article.

            IMPORTANT:
            The selected perspective is: {perspective}.
            The Bias Score, Bias Direction, Sentiment, Loaded Language, and Evidence Quality Score must be determined objectively from the article itself and MUST NOT change simply because a different perspective is selected.

            The selected perspective should only affect:
            - Selected Perspective Analysis
            - Opposing Perspective Analysis
            - Perspective Rewrite

            Return the result in EXACTLY this format.

            Bias Score: <0-100>
            Bias Direction: <Left Leaning / Right Leaning / Neutral>
            Sentiment: <Positive / Negative / Neutral>
            Loaded Language Detected:
            - word/phrase 1
            - word/phrase 2
            - word/phrase 3
            Evidence Quality Score: <0-100>
            Reasoning: <Explain reasoning>
            Selected Perspective Analysis: <Explain viewpoint>
            Opposing Perspective Analysis: <Explain opposing viewpoint>
            Neutral Rewrite: <Rewrite objectively>
            Perspective Rewrite: <Rewrite from {perspective} perspective>
            Key Takeaways:
            - Point 1
            - Point 2
            - Point 3
            Article: {user_input}
            """

            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(prompt)

                st.success("✅ Analysis Complete")
                st.markdown("<div class='neon-header'>Analysis Result</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='analysis-output'>{response.text}</div>", unsafe_allow_html=True)

                # --- Bias Direction ---
                st.markdown("<div class='neon-header'>Bias Direction</div>", unsafe_allow_html=True)
                if "Left" in response.text:
                    st.write("⬅️ Left Leaning")
                elif "Right" in response.text:
                    st.write("➡️ Right Leaning")
                else:
                    st.write("⚖️ Neutral")

                # --- Evidence Quality Meter ---
                try:
                    eq_line = response.text.split("Evidence Quality Score:")[1].split("\n")[0]
                    eq_score = int(eq_line.strip())
                    st.markdown("<div class='neon-header'>Evidence Quality</div>", unsafe_allow_html=True)
                    st.progress(eq_score)
                except:
                    st.info("Could not extract evidence quality score.")

                # --- Perspective Comparison ---
                st.markdown("<div class='neon-header'>Perspective Comparison</div>", unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("<div class='neon-header'>Selected Perspective</div>", unsafe_allow_html=True)
                    st.write(response.text.split("Selected Perspective Analysis:")[1].split("Opposing")[0])
                with col2:
                    st.markdown("<div class='neon-header'>Opposing Perspective</div>", unsafe_allow_html=True)
                    st.write(response.text.split("Opposing Perspective Analysis:")[1].split("Neutral Rewrite:")[0])

                # --- Collapsible Sections ---
                with st.expander("Neutral Rewrite"):
                    st.write(response.text.split("Neutral Rewrite:")[1].split("Perspective Rewrite:")[0])
                with st.expander("Perspective Rewrite"):
                    st.write(response.text.split("Perspective Rewrite:")[1].split("Key Takeaways:")[0])
                with st.expander("Key Takeaways"):
                    st.write(response.text.split("Key Takeaways:")[1])

                # --- Bias Meter ---
                try:
                    score_line = response.text.split("Bias Score:")[1].split("\n")[0]
                    bias_score = int(score_line.strip())
                    st.markdown("<div class='neon-header'>Bias Meter</div>", unsafe_allow_html=True)
                    st.progress(bias_score)
                    if bias_score <= 20:
                        label = "Low Bias"
                    elif bias_score <= 50:
                        label = "Slight Bias"
                    elif bias_score <= 75:
                        label = "Moderate Bias"
                    else:
                        label = "High Bias"
                except:
                    st.info("Could not generate bias meter.")

            
            except Exception as e:
                error_message = str(e)
                if "429" in error_message or "quota" in error_message.lower():
                    st.error("🚫 Gemini API quota exceeded. Please wait a bit or check your API usage at [ai.dev/rate-limit](https://ai.dev/rate-limit).")
                    st.info("Tip: You can upgrade your plan or switch to a new API key to continue using Reality Lens AI.")
                else:
                    st.error("⚠️ Something went wrong while analyzing. Please try again later.")


# --- Test Gemini Button ---
if st.button("Test Gemini"):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content("Explain media bias in one sentence.")
        st.success("✅ Gemini Connected!")
        st.write(response.text)
    except Exception as e:
        st.error(f"Gemini Error: {e}")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Built with Streamlit + Gemini AI 🚀</p>", unsafe_allow_html=True)
