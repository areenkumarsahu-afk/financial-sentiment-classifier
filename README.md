# Financial Sentiment Classifier 
This project uses a fine-tuned BERT model ('yiyanghkust/finbert-tone') from Hugging Face Transformers to predict the sentiment of financial text (positive, negative, or neutral).

## What It Does
Given a sentence (like a news headline or report snippet), the model predicts if the sentiment is:
- Positive
- Negative
- Neutral

## Model Used 
- Model:
['yiyanghkust/finbert-tone'](https://huggingface.co/yiyanghkust/finbert-tone)
- Library: Hugging Face 'transformers', 'torch'