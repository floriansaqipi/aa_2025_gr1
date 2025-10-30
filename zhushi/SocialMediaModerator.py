#!/usr/bin/env python3

def flag(post: str, bad_words: list[str]) -> (bool, str):
    clean_post = (post.lower()
                  .replace("_", "")
                  .replace(" ", "")
                  .replace("-", "")
                  .replace(".", "")
                  .replace("!", "")
                  )

    for badword in bad_words:
        # print(f"badword = {badword}; clean_post = {clean_post}")
        if badword in clean_post:
            return (True, badword)
    return (False, " ")

def main(posts: list[str], bad_words: list[str]) -> list[bool]:
    output = []
    for post in posts:
        (is_flagged, badword) = flag(post, bad_words)
        if is_flagged:
            output.append(f"FLAGGED - Contains: [\"{badword}\"]")
        else:
            output.append("CLEAN")
    return output

if __name__ == '__main__':
    posts = [
        "Check out my new recipe for chocolate cake!",
        "CLICK HERE NOW for amazing deals!!!",
        "I don't agree with that hate speech in the comments",
        "Buy_Followers cheap and fast delivery",
        "This is a normal post about my day"
    ]

    bad_words = [
        "hate speech",
        "buy followers",
        "click here now",
        "banned content",
        "illegal drugs"
    ]

    for i in range(len(bad_words)):
        bad_words[i] = bad_words[i].replace(" ", "")

    outputs = main(posts, bad_words)

    for output in outputs:
        print(output)