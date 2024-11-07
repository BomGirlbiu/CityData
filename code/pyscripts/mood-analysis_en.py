from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", tokenizer="facebook/bart-large-mnli")

sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing', 'exploration']
result=classifier(sequence_to_classify, candidate_labels, multi_label=True)
print(result)