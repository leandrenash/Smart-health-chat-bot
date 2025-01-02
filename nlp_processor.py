import spacy
from typing import Dict, List
import re

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # Fallback to basic string processing if spaCy model isn't available
    nlp = None

def process_text(text: str) -> Dict:
    """Process input text using NLP techniques."""
    processed = {
        "text": text,
        "keywords": extract_keywords(text),
        "entities": extract_entities(text)
    }
    return processed

def extract_keywords(text: str) -> List[str]:
    """Extract relevant keywords from the input text."""
    if nlp:
        # Use spaCy for keyword extraction
        doc = nlp(text.lower())
        keywords = []
        
        # Extract nouns and adjectives
        for token in doc:
            if token.pos_ in ["NOUN", "ADJ"] and not token.is_stop:
                keywords.append(token.text)
        
        # Extract noun phrases
        for chunk in doc.noun_chunks:
            keywords.append(chunk.text)
    else:
        # Fallback to basic word splitting
        keywords = text.lower().split()
    
    # Clean and deduplicate keywords
    keywords = list(set(keywords))
    keywords = [k.strip() for k in keywords if len(k.strip()) > 2]
    
    return keywords

def extract_entities(text: str) -> List[str]:
    """Extract named entities from the text."""
    if nlp:
        doc = nlp(text)
        entities = []
        for ent in doc.ents:
            if ent.label_ in ["SYMPTOM", "CONDITION", "BODY_PART"]:
                entities.append(ent.text)
        return entities
    return []

def preprocess_text(text: str) -> str:
    """Preprocess text by removing special characters and normalizing."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
