from transformers import XLNetTokenizer, XLNetForSequenceClassification
from torch.nn.functional import softmax
import torch

# Step 1: Load XLNet tokenizer and model
tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
model = XLNetForSequenceClassification.from_pretrained('xlnet-base-cased')

# Step 2: Preprocess the input text
text = "You look like shit"
inputs = tokenizer(text, return_tensors="pt")

# Step 3: Make predictions
with torch.no_grad():
    outputs = model(**inputs)

# Step 4: Get the predicted probabilities
logits = outputs.logits
probs = softmax(logits, dim=1)

# Step 5: Print the results
predicted_class = torch.argmax(probs, dim=1).item()
print(f"Predicted Class: {predicted_class}")
print(f"Class Probabilities: {probs.tolist()}")
