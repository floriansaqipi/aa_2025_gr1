import re

# Blacklisted phrases
blacklist = [
    "hate speech",
    "buy followers",
    "click here now",
    "banned content",
    "illegal drugs"
]

# Posts to check
posts = [
    "Check out my new recipe for chocolate cake!",
    "CLICK HERE NOW for amazing deals!!!",
    "I don't agree with that hate speech in the comments",
    "Buy_Followers cheap and fast delivery",
    "This is a normal post about my day"
]

def preprocess(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def check_post(post, blacklist):
    post_processed = preprocess(post)
    found_phrases = []

    for phrase in blacklist:
        phrase_processed = preprocess(phrase)
        if phrase_processed in post_processed:
            found_phrases.append(phrase)

    if found_phrases:
        return f"FLAGGED Contains: {found_phrases}"
    else:
        return "CLEAN"

for i, post in enumerate(posts, 1):
    result = check_post(post, blacklist)
    print(f"Post {i}: {result}")
