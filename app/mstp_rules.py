import spacy
import re

nlp = spacy.load("en_core_web_sm")

def analyze_content(content):
    doc = nlp(content)
    suggestions = []

    # MSTP Rule: Avoid passive voice
    for sentence in doc.sents:
        if any(tok.dep_ == "auxpass" for tok in sentence):
            suggestions.append(f"Consider revising this sentence to active voice: {sentence.text.strip()}")

    # MSTP Rule: Detect double spaces
    lines = content.split('\n')
    for line in lines:
        if '  ' in line:
            suggestions.append(f"Remove double spaces in the following sentence: {line.strip()}")

    return suggestions
