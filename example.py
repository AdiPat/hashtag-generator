from hashtag_utils import HashtagUtils

## 1. with default args
hg = HashtagUtils()

text = "A new study shows that eating chocolate can help you lose weight."

hashtags = hg.get_hashtags(text)

print("text: ", text)
print("hashtags returned: ", hashtags)

## 2. with custom args

text = """Error messages can teach you a lot! ♨️ 

When programming, coming across errors is common. You probably see an error everyday when writing code and spend time debugging it. How many times do we actually spend time understanding the error message, stack trace and it's causes before checking StackOverflow or asking CoPilot? Not many times. 

While getting quick help and resolving errors quickly without gaining much understanding might help you move faster in the short-term, it hinders your learning. When you spend time understanding the error message and stack trace, you gain insight into "what's happening behind the scenes". This improves your knowledge and ability to use the programming language or in short, technology.

Having understanding of the various types of errors your program can throw helps you design better error handling. You can design systems to handle errors systematically and check for all the correct conditions so that your code responds to failures gracefully.

In some cases, exploring the stack trace might take you down a rabbit hole and you could lose broader context. In such cases, it might be practical to employ a "quick fix", but don't be hasty - make sure you have thought out and made sense of the error, why it happened, and how to prevent it in future.

This will improve your ability to be useful oncall. When errors come up in production, make sure you have good logging and monitoring so that all the data you need to debug is easily available to you. This, combined with good "error reading skills" will take you a long way.

What's your process to solve errors when programming? Let me know in the comments section. ✨ """

hashtags = hg.get_hashtags(text, temperature=0.7, num_tags=10)

print("text: ", text)
print("hashtags returned: ", hashtags)

### 3. Similar hashtags

hashtags = ["#ProductEngineering", "#Tech", "#HackerCulture"]

similar_hashtags = hg.get_similar_hashtags(hashtags, temperature=0.7, num_tags=10)

print("hashtags: ", hashtags)
print("similar hashtags", similar_hashtags)

## 4. Hashtag Definitions

hashtags = [
    "#ProductEngineering",
    "#Tech",
    "#HackerCulture",
    "Productivity",
    "LOL",
    "AI",
    "MVP",
]

[print(hg.get_hashtag_definition(hashtag)) for hashtag in hashtags]
