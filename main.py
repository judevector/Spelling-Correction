from textblob import TextBlob
def convert(string):
    li = list(string.split())
    return li
fword = input("Enter your word here: ")
words = convert(fword)
corrected_words = []

for _ in words:
    corrected_words.append(TextBlob(_))
    print("Your wrong word: ", words)
    print("Corrected words are: ")
