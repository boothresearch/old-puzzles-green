import re

def abbreviate(words):
    if "'s"  in words:
         words=words.replace("'s","")
    temp=re.split('[^a-zA-Z]', words)
    new_temp=[]
    for i in range(len(temp)):
        if temp[i]!="":
            new_temp.append(temp[i])
    new_temp=[new_temp[i][0].upper() if new_temp[i][0].isalpha() else "" for i in range(len(new_temp))]
    return ''.join(new_temp)

    

    
