import difflib
import random

intents = {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey", "good morning", "good evening"
        ],
        "responses": [
            "Hello there.",
            "Hi, how can I help you?",
            "Hey. I’m here.",
            "Greetings."
        ]
    },
    "peace": {
        "patterns": [
            "peace upon you", "peace be upon you", "salam"
        ],
        "responses": [
            "Peace be upon you too.",
            "And peace to you.",
            "May peace be with you."
        ]
    },
    "identity": {
        "patterns": [
            "are you a robot", "are you human"
        ],
        "responses": [
            "I am an artificial intelligence.",
            "I’m a digital entity, not human.",
            "I exist as software."
        ]
    },
    "name": {
        "patterns": [
            "what is your name", "your name"
        ],
        "responses": [
            "My name is Whitefurry.",
            "You can call me Whitefurry.",
            "I’m known as Whitefurry."
        ]
    },
    "creator": {
        "patterns": [
            "who made you", "who created you"
        ],
        "responses": [
            "I was created by a human developer.",
            "A human mind designed me.",
            "I am a product of human code."
        ]
    }
}

all_patterns = []
pattern_to_intent = {}

for intent, data in intents.items():
    for p in data["patterns"]:
        all_patterns.append(p)
        pattern_to_intent[p] = intent

def detect_intent(text):
    text = text.lower()
    match = difflib.get_close_matches(text, all_patterns, n=1, cutoff=0.5)
    if not match:
        return None
    return pattern_to_intent[match[0]]

def whitefurry():
    print("Whitefurry 1.0 🤖")
    while True:
        user = input("\nYou: ").strip()
        if user.lower() == "exit":
            print("Whitefurry: Goodbye.")
            break
        intent = detect_intent(user)
        if intent:
            print("Whitefurry:", random.choice(intents[intent]["responses"]))
        else:
            print("Whitefurry: I’m not sure I understand yet.")

if __name__ == "__main__":
    whitefurry()
  
