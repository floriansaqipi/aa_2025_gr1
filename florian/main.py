import re


def normalize_text(text):
    return re.sub(r'[^a-z0-9 ]', '', text.lower())


def flag_posts(blacklisted_phrases, posts):
    normalized_blacklist = set()
    for phrase in blacklisted_phrases:
        normalized_phrase = normalize_text(phrase).replace(" ", "")
        normalized_blacklist.add(normalized_phrase)

    results = []
    for idx, post in enumerate(posts, start=1):
        normalized_post = normalize_text(post).replace(" ", "")
        found_phrases = []

        for phrase in normalized_blacklist:
            if phrase in normalized_post:
                for original_phrase in blacklisted_phrases:
                    if normalize_text(original_phrase).replace(" ", "") == phrase:
                        found_phrases.append(original_phrase)
                        break

        if found_phrases:
            results.append(f"Post {idx}: FLAGGED - Contains: {found_phrases}")
        else:
            results.append(f"Post {idx}: CLEAN")

    return results


# Example usage
blacklisted_phrases = ["hate speech", "buy followers", "click here now", "banned content", "illegal drugs"]
posts = [
    "Check out my new recipe for chocolate cake!",
    "CLICK HERE NOW for amazing deals!!!",
    "I don't agree with that hate speech in the comments",
    "Buy_Followers cheap and fast delivery",
    "This is a normal post about my day"
]

output = flag_posts(blacklisted_phrases, posts)
for line in output:
    print(line)
