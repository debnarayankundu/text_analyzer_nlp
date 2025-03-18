import streamlit as st
import pandas as pd
import torch
from transformers import pipeline
import PyPDF2

def extract_text(file):
    """Extracts text from an uploaded file (CSV, PDF, or TXT)."""
    text_data = ""
    
    if file.name.endswith(".csv"):  
        df = pd.read_csv(file)
        text_data = df.to_string()
    elif file.name.endswith(".pdf"):  
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text_data += page.extract_text() + " "
    else:  
        text_data = str(file.read(), "utf-8")
    
    return text_data if text_data else 'Error: Invalid input format or empty file.'

def summarize_text(text_data, length_ratio):
    original_length = len(text_data.split())
    target_length = max(50, min(200, int(original_length * length_ratio)))
    
    summarizer = pipeline("summarization")
    
    summaries = []
    for i in range(0, len(text_data), 1000):
        chunk = text_data[i:i+1000]
        summary = summarizer(chunk, max_length=target_length, min_length=max(25, target_length // 2), do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)

def analyze_sentiment(text_data):
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiment = sentiment_analyzer(text_data)    
    return sentiment[0]

def named_entity_recognition(text_data):
    """Performs Named Entity Recognition (NER) and formats output."""
    ner_pipeline = pipeline("ner", aggregation_strategy="simple")
    entities = ner_pipeline(text_data)
    
    formatted_entities = {}
    for entity in entities:
        entity_name = entity['word']  
        entity_type = entity['entity_group']  
        
        if entity_type not in formatted_entities:
            formatted_entities[entity_type] = set()
        formatted_entities[entity_type].add(entity_name)
    
    return {key: list(value) for key, value in formatted_entities.items()}


st.title("AI-Powered Text Processing Web App")

option = st.radio("Choose a task:", ("Summarization", "Sentiment Analysis", "Named Entity Recognition (NER)"))

if option == "Summarization":
    text_input = st.text_area("Enter text for summarization (optional):")
    uploaded_file = st.file_uploader("Upload a CSV, PDF, or TXT file", type=["csv", "pdf", "txt"])
    length_ratio = st.slider("Select summary length (as a fraction of original text):", 0.2, 0.7, 0.4, 0.05)
    
    text_data = ""
    if uploaded_file:
        text_data = extract_text(uploaded_file)
    if text_input:
        text_data = text_input
    
    if text_data:
        summary = summarize_text(text_data, length_ratio)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter text or upload a file for summarization.")

else:
    text_input = st.text_area("Enter text for processing (optional):")
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    
    text_data = ""
    if uploaded_file:
        text_data = extract_text(uploaded_file)
    if text_input:
        text_data = text_input
    
    if text_data:
        if option == "Sentiment Analysis":
            sentiment = analyze_sentiment(text_data)
            st.subheader("Sentiment Analysis:")
            st.write(sentiment)
        elif option == "Named Entity Recognition (NER)":
            entities = named_entity_recognition(text_data)
            st.subheader("Named Entities:")
            for entity_type, entity_list in entities.items():
                st.write(f"**{entity_type}:** {', '.join(entity_list)}")
    else:
        st.warning("Please enter text or upload a file for processing.")