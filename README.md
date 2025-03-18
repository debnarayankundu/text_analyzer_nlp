# AI-Powered Text Processing Web App

## Overview
This Streamlit-based web application provides advanced text processing features using Transformer-based deep learning models. Users can perform:
- **Summarization**: Generate concise summaries from text, PDFs, CSVs, or TXT files.
- **Sentiment Analysis**: Determine the sentiment (positive, negative, or neutral) of input text.
- **Named Entity Recognition (NER)**: Identify named entities (e.g., people, organizations, locations) in text.

## Features
- Upload and process **CSV, PDF, and TXT** files for summarization.
- Adjustable **summary length slider** (20% to 70% of the original text).
- Perform **Sentiment Analysis** on entire texts.
- Extract and merge **Named Entities (NER)** for clear output.
- Streamlit-based interactive UI for easy usage.

## Installation
### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/debnarayankundu/text_analyzer_nlp.git
   cd text_analyzer_nlp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Select a processing task (Summarization, Sentiment Analysis, NER).
2. Provide input text or upload a file (PDF, CSV, or TXT).
3. For summarization, adjust the summary length using the slider.
4. Click the submit button to process the text and view the results.

## Dependencies
- `streamlit`
- `pandas`
- `torch`
- `transformers`
- `PyPDF2`

Install them using:
```bash
pip install streamlit pandas torch transformers PyPDF2
```

![image](https://github.com/user-attachments/assets/f5fd999d-b727-43ba-b2e4-33305a0b22b5)



