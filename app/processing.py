import re
import os
import preprocessor as p
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def clean_sentence(text):
        text = p.clean(text)
        text = re.sub(r"[^a-zA-Z0-9]+", " ", text) 
        return text

def analyze_sentence(text):
    saved_model_path = "saved-model"
    model_name = "mdhugol/indonesia-bert-sentiment-classification"
    
    def sentiment(text):
        result = sentiment_analysis(text)
        status = label_index[result[0]["label"]]
        return status
        
    def sentiment_score(text):
        result = sentiment_analysis(text)
        score = result[0]["score"]
        return score

    if os.path.exists(saved_model_path):
        print("Loading pretrained model from local storage...")
        tokenizer = AutoTokenizer.from_pretrained(saved_model_path)
        model = AutoModelForSequenceClassification.from_pretrained(saved_model_path)
        sentiment_analysis = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        label_index = {"LABEL_0": "positive", "LABEL_1": "neutral", "LABEL_2": "negative"}
        
        sentiment_data = {}
        sentiment_data['sentiment'] = sentiment(text)
        sentiment_data['sentiment_score'] = sentiment_score(text)
    else:
        print("Downloading and saving pretrained model...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        sentiment_analysis = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        label_index = {"LABEL_0": "positive", "LABEL_1": "neutral", "LABEL_2": "negative"}
        
        sentiment_data = {}
        sentiment_data['sentiment'] = sentiment(text)
        sentiment_data['sentiment_score'] = sentiment_score(text)
        
        tokenizer.save_pretrained(saved_model_path)
        model.save_pretrained(saved_model_path)
    return sentiment_data