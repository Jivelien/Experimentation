import string
def is_pangram(sentence):
    sentence=sentence.lower()
    pangram=True
    for letter in string.ascii_lowercase:
        if letter not in sentence:
            pangram=False
    return pangram