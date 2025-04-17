import sys
import time
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


start = time.time()
# Get input text from command-line argument
user_input = sys.argv[1]

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", trust_remote_code=True)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Run classification
result = classifier(user_input)[0]

# Print result to stdout
print(f"Label: {result['label']}")
print(f"Confidence: {result['score']:.4f}")
end = time.time()
print(f"Inference time: {end - start:.2f} seconds")
