import random
from words import words

def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

get_word()
print(get_word())