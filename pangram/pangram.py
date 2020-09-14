def is_pangram(sentence):
    s=set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t","u","v","w","x","y","z"])
    sentence=sentence.lower()
    for i in range(len(sentence)):
        if sentence[i] in s:
            s.remove(sentence[i])

    return len(s)==0

    
