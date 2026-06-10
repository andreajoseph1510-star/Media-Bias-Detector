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

# --- Custom CSS for Black-Green Theme ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

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
        color: #00ccff;                     /* light neon blue */
        text-shadow: 0 0 8px #00ccff, 0 0 16px #00ccff;
        font-size: 16px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    /* --- Improve readability for analysis output --- */
    .analysis-output {
        font-family: 'VT323', monospace;
        font-size: 13px;
        line-height: 1.6;
        color: #00cc00;
        background-color: #0a0a0a;
        border: 1px solid #00ff00;
        border-radius: 6px;
        padding: 15px;
        margin-top: 15px;
        margin-bottom: 15px;
        white-space: pre-wrap;
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
        <h1>🌎 Reality Lens AI</h1>
        <p>See Every Side of the Story</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Input Section ---
st.subheader("Paste or Upload Media Content")

user_input = st.text_area(
    "Enter article, post, or snippet:",
    height=200
)

uploaded_file = st.file_uploader(
    "Or upload a text file",
    type=["txt"]
)

if uploaded_file is not None:
    user_input = uploaded_file.read().decode("utf-8")

# --- Perspective Selection ---
st.subheader("Perspective Comparison")

perspective = st.selectbox(
    "Choose a perspective",
    [
        "Neutral",
        "Progressive",
        "Conservative",
        "Optimistic",
        "Pessimistic"
    ]
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

        When writing the "Selected Perspective Analysis" section, explain how a person with a {perspective} viewpoint would interpret this article.

        When writing the "Perspective Rewrite" section, rewrite the article from the {perspective} perspective while keeping it realistic and consistent with that viewpoint.

        Return the result in EXACTLY this format.

        Bias Score: <0-100>

        Bias Direction:
        <Left Leaning / Right Leaning / Neutral>

        Sentiment:
        <Positive / Negative / Neutral>

        Loaded Language Detected:
        - word/phrase 1
        - word/phrase 2
        - word/phrase 3

        Evidence Quality Score:
        <0-100>

        Reasoning:
        <Explain why the article received this score and how the selected perspective might evaluate the framing>

        Selected Perspective Analysis:
        <Explain how someone with a {perspective} viewpoint would interpret this article>

        Opposing Perspective Analysis:
        <Explain how someone with an opposing viewpoint would interpret this article>

        Neutral Rewrite:
        <Rewrite the article objectively and without bias>

        Perspective Rewrite:
        <Rewrite the article from the {perspective} perspective>

        Key Takeaways:
        - Point 1
        - Point 2
        - Point 3

        Article:
        {user_input}
        """

            try:
                model = genai.GenerativeModel("gemini-2.5-flash")

                response = model.generate_content(prompt)

                st.success("✅ Analysis Complete")

                st.markdown("## Analysis Result")
                st.write(response.text)
                # --- Bias Direction Indicator ---
                st.subheader("Bias Direction")
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
                    st.subheader("Evidence Quality")
                    st.progress(eq_score)
                except:
                    st.info("Could not extract evidence quality score.")

                # --- Multi-Column Perspective Comparison ---
                st.subheader("Perspective Comparison")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### Selected Perspective")
                    st.write(response.text.split("Selected Perspective Analysis:")[1].split("Opposing")[0])
                with col2:
                    st.markdown("### Opposing Perspective")
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
                    score_line = response.text.split(
                        "Bias Score:"
                    )[1].split("\n")[0]

                    bias_score = int(score_line.strip())

                    st.subheader("Bias Meter")

                    st.progress(bias_score)

                    if bias_score < 30:
                        st.success("🟢 Low Bias")

                    elif bias_score < 70:
                        st.warning("🟡 Moderate Bias")

                    else:
                        st.error("🔴 High Bias")

                except:
                    st.info("Could not generate bias meter.")

            except Exception as e:
                st.error(f"Error: {e}")

# --- Test Gemini Button ---
if st.button("Test Gemini"):

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            "Explain media bias in one sentence."
        )

        st.success("✅ Gemini Connected!")
        st.write(response.text)

    except Exception as e:
        st.error(f"Gemini Error: {e}")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;'>Built with Streamlit + Gemini AI 🚀</p>",
    unsafe_allow_html=True
)