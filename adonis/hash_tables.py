import re

# Blacklisted phrases
blacklist = [
    "hate speech",
    "buy followers",
    "click here now",
    "banned content",
    "illegal drugs",
    "hate"
]

# Posts to check
posts = [
    "Check out my new recipe for chocolate cake!",
    "CLICK HERE NOW for amazing deals!!!",
    "I don't agree with that hate speech in the comments",
    "Buy_Followers cheap and fast delivery",
    "This is a normal post about my day",
    "I hate injustice"
]

def preprocess(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def is_context_positive(post):
    positive_context = ["injustice", "crime", "poverty", "violence", "discrimination"]
    post_lower = post.lower()
    for word in positive_context:
        if word in post_lower:
            return True
    return False


def check_post(post, blacklist):
    post_processed = preprocess(post)
    found_phrases = []

    for phrase in blacklist:
        phrase_processed = preprocess(phrase)
        if phrase_processed in post_processed:
            if phrase_processed == "hate" and is_context_positive(post):
                continue
            found_phrases.append(phrase)

    if found_phrases:
        return f"FLAGGED Contains: {found_phrases}"
    else:
        return "CLEAN"

for i, post in enumerate(posts, 1):
    result = check_post(post, blacklist)
    print(f"Post {i}: {result}")
