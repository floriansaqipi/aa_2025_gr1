

def flag_posts(blacklisted_phrases, posts):

    blacklist_set = set()
    for phrase in blacklisted_phrases:
        blacklist_set.add(phrase.lower())


    for i in range(len(posts)):
        post = posts[i]
        post_lower = post.lower()


        found_phrases = []

        for phrase in blacklist_set:
            if phrase in post_lower:
                found_phrases.append(phrase)

        if len(found_phrases) > 0:
            print(f"Post {i + 1}: FLAGGED - Contains: {found_phrases}")
        else:
            print(f"Post {i + 1}: CLEAN")



blacklisted_phrases = [
    "hate speech",
    "buy followers",
    "click here now",
    "banned content",
    "illegal drugs"
]

posts = [
    "Check out my new recipe for chocolate cake!",
    "CLICK HERE NOW for amazing deals!!!",
    "I don't agree with that hate speech in the comments",
    "Buy_Followers cheap and fast delivery",
    "This is a normal post about my day"
]


flag_posts(blacklisted_phrases, posts)
