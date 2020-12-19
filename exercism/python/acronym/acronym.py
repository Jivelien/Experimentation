import re

def abbreviate(words):
    words=re.sub('[^a-zA-Z -]+', '',words)
    letterList=[]
    for word in re.split(" |-",words):
        if len(word)>0:
             letterList.append(word[0])
    acronym="".join(letterList)
    acronym=acronym.upper()
    return acronym
