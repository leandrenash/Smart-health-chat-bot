from typing import Dict, List, Set
import re

# Medical knowledge base
COMMON_ILLNESSES: Dict[str, Dict] = {
    "common_cold": {
        "symptoms": ["runny nose", "cough", "sore throat", "fever", "congestion"],
        "remedies": [
            "Rest well and get adequate sleep",
            "Stay hydrated with water and warm fluids",
            "Use over-the-counter cold medications",
            "Try salt water gargle for sore throat"
        ],
        "severity": "mild"
    },
    "flu": {
        "symptoms": ["high fever", "body aches", "fatigue", "cough", "headache"],
        "remedies": [
            "Get plenty of rest",
            "Stay hydrated",
            "Take acetaminophen for fever",
            "Use humidifier"
        ],
        "severity": "moderate"
    },
    "allergies": {
        "symptoms": ["sneezing", "itchy eyes", "runny nose", "congestion"],
        "remedies": [
            "Avoid known allergens",
            "Use air purifiers",
            "Try over-the-counter antihistamines",
            "Keep windows closed during high pollen times"
        ],
        "severity": "mild"
    }
}

EMERGENCY_KEYWORDS: Set[str] = {
    "chest pain", "difficulty breathing", "severe bleeding",
    "unconscious", "stroke", "heart attack", "seizure",
    "severe allergic reaction", "anaphylaxis"
}

def generate_response(processed_input: Dict) -> str:
    """Generate appropriate response based on processed input."""
    keywords = processed_input["keywords"]
    
    # Check for matches in common illnesses
    possible_conditions = []
    for illness, data in COMMON_ILLNESSES.items():
        if any(symptom in keywords for symptom in data["symptoms"]):
            possible_conditions.append((illness, data))
    
    if not possible_conditions:
        return generate_general_response()
    
    # Generate response for matched conditions
    response = "Based on the symptoms you've described:\n\n"
    for illness, data in possible_conditions:
        response += f"**Possible condition: {illness.replace('_', ' ').title()}**\n"
        response += "Common remedies:\n"
        for remedy in data["remedies"]:
            response += f"- {remedy}\n"
        response += f"\nSeverity level: {data['severity']}\n\n"
    
    response += "\n⚠️ Remember: This is general information only. Please consult a healthcare professional for proper diagnosis and treatment."
    return response

def generate_general_response() -> str:
    """Generate a general response when no specific condition is matched."""
    return """I understand you're not feeling well. While I can't determine your specific condition, here are some general health tips:

- Get adequate rest
- Stay hydrated
- Monitor your symptoms
- Maintain good hygiene

Please consult a healthcare professional if your symptoms persist or worsen."""

def is_emergency(processed_input: Dict) -> bool:
    """Check if the input contains emergency keywords."""
    return any(keyword in processed_input["text"].lower() for keyword in EMERGENCY_KEYWORDS)
