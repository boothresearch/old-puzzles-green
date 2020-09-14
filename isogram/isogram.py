def is_isogram(string):
    test_dict={}
    string=string.lower()
    for i in range(len(string)):
        if string[i]!="-" and string[i]!=" ":
            if string[i] in test_dict:
                return False
            else:
                test_dict[string[i]]=1
    return True
    
