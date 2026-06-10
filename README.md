# Reality Lens AI

## Overview

Reality Lens AI is an AI-powered media analysis platform that helps users identify bias, sentiment, framing techniques, and perspective differences in news articles and online content.

The application analyzes articles using advanced language models and presents multiple viewpoints to encourage critical thinking and media literacy.

Built for the **GitHub Copilot Creative Apps Challenge**, Reality Lens AI demonstrates how AI can be used to improve information awareness and help users understand how narratives change across perspectives.

---

## Problem Statement

Modern media consumers are exposed to information from thousands of sources every day. News articles often contain subtle bias, emotional framing, selective language, and one-sided narratives that can influence public opinion.

Most readers do not have the time or tools to objectively evaluate these biases.

Reality Lens AI helps users:

* Detect potential bias in articles
* Understand sentiment and framing
* Compare alternative viewpoints
* View objective rewrites of content
* Improve media literacy and critical thinking

---

## Features

### Bias Detection

Generates a Bias Score (0–100) indicating the level of bias present in the article.

### Bias Direction Analysis

Identifies whether content appears:

* Left Leaning
* Right Leaning
* Neutral

### Sentiment Analysis

Determines the emotional tone of the content:

* Positive
* Negative
* Neutral

### Loaded Language Detection

Highlights emotionally charged words and phrases that may influence reader perception.

### Evidence Quality Scoring

Evaluates how strongly the article supports its claims with evidence and factual information.

### Multi-Perspective Analysis

Provides:

* Supporter Perspective
* Critic Perspective

to help users understand how different audiences may interpret the same article.

### Perspective Comparison

Users can generate analysis from different viewpoints:

* Neutral
* Progressive
* Conservative
* Optimistic
* Pessimistic

### Neutral Rewrite

Creates an objective and balanced version of the article while preserving the core facts.

### Key Takeaways

Summarizes the most important points from the content.

### Bias Meter Visualization

Displays a visual representation of article bias using Streamlit components.

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 2.5 Flash

### Development Tools

* GitHub Copilot
* VS Code

### Configuration

* Python Dotenv

---

## Architecture

User Input
↓
Reality Lens AI
↓
Prompt Engineering Layer
↓
Gemini 2.5 Flash
↓
Bias Analysis Engine
↓
Perspective Analysis Engine
↓
Visualization Layer
↓
Final Report

---

## GitHub Copilot Usage

GitHub Copilot was used extensively during development for:

* Streamlit UI generation
* Python code suggestions
* Debugging assistance
* API integration support
* Prompt engineering refinement
* Code explanation and optimization

Examples of Copilot-assisted development include:

* Building the Streamlit interface
* Creating Gemini API integration
* Developing perspective analysis features
* Debugging application errors
* Improving code readability and structure

---

## Microsoft IQ Integration

Reality Lens AI is designed around the principles of Microsoft's Foundry IQ intelligence layer.

The application uses grounded multi-perspective reasoning to:

* Reduce informational bias
* Encourage evidence-based interpretation
* Compare competing narratives
* Improve understanding of complex topics

The architecture supports future integration with Microsoft Foundry IQ retrieval systems for citation-backed and grounded analysis.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/reality-lens-ai.git
cd reality-lens-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Screenshots

### Home Screen

(Add screenshot)

### Analysis Results

(Add screenshot)

### Perspective Comparison

(Add screenshot)

---

## Future Improvements

* Real-time fact verification
* Source reliability scoring
* Multi-language support
* News source comparison
* Citation-backed evidence retrieval
* Historical narrative comparison
* Advanced media literacy insights

---

## Challenges Faced

* Prompt optimization for consistent analysis
* Bias measurement calibration
* Multi-perspective generation
* API quota limitations
* Building a clear and intuitive user interface

---

## Impact

Reality Lens AI promotes responsible media consumption by helping users:

* Recognize bias
* Evaluate evidence
* Understand alternative viewpoints
* Make informed decisions

The project aims to improve digital literacy and encourage critical thinking in an increasingly information-driven world.

---

## License

MIT License

---

## Author

Developed by Andrea Maria Joseph
