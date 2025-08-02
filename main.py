from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch

tokenizer=AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model=AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")
def predict_sentiment(text):
    inputs=tokenizer(text,return_tensors="pt",truncation=True)
    with torch.no_grade:
        outputs=model(**inputs)
    logits=outputs.logits
    predicted_class_id=torch.agrmax(logits).item()
    labels=["positive","negative","neutral"]
    return labels[predicted_class_id]