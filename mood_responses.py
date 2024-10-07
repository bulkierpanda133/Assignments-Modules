# mood_responses.py

def mood_response(mood):
    # Dictionary mapping moods to responses
    responses = {
        'happy': "That's great! Keep smiling and spread the joy!",
        'sad': "I'm sorry to hear that. I hope things get better soon.",
        'excited': "Awesome! I hope you enjoy your day full of excitement!",
        'angry': "Take a deep breath. It's okay to be angry sometimes.",
        'nervous': "It's okay to feel nervous. You've got this!",
        'tired': "You should get some rest. Self-care is important!",
        'bored': "Maybe try something new to spice things up!",
        'confused': "I understand, take your time to figure things out."
    }
# Normalize the input and provide a default response if mood is not recognized
    mood = mood.lower()
    return responses.get(mood, "I'm not sure how to respond to that, but I hope you're doing well!")


