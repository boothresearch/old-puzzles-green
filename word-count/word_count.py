import re


def count_words(sentence):
    sentence=sentence.lower()
    sentence= " ".join(sentence.split())
    sentence = re.split("[^a-zA-Z0-9|'t|'s|'ve]", sentence)
    sentence=[sentence[i].strip() for i in range(len(sentence))]
    result={}
    for i in range(len(sentence)):
        if sentence[i]!="" :
            if sentence[i][0]=="'" and sentence[i][-1]=="'":
                sentence[i]= sentence[i].replace("'", "")
            if sentence[i] in result:
                result[sentence[i]]+=1
            else:
                result[sentence[i]]=1

    return result 


#count_words("one fish two fish red fish blue fish")

