def num99(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    twenties = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 
        'seventy', 'eighty', 'ninety']
    # single digit
    b = n % 10
    # tens digit
    a = ((n%100) - b) / 10
    
    result = ''
    if 0 <= n and n <= 99:
        if a == 1:
            c = 10 + b
            result = ones[c]
        elif a == 0:
            result = ones[b]
        else:
            result = twenties[a] + '-' + ones[b]
    else:
        result = 'Number not in the range!'

    return(result)

def num_chunks(n):
    chunks = []
    num = f'{n:,}'
    chunks = num.split(',')
    if len(chunks) > 4:
        return('Number not in range!')
    else:
        for i in range(len(chunks)):
            chunks[i] = int(chunks[i])
        return(chunks)
    
def scale_words(chunks):
    thousands = ['', 'thousand', 'million', 'billion']
    if len(chunks) == 1:
        return(str(chunks[0]))
    elif len(chunks) == 2:
        return(str(chunks[1]) + thousands[1] + str(chunks[0]))
    elif len(chunks) == 3:
        return(str(chunks[2]) + thousands[2] + str(chunks[1]) + thousands[1] + 
                str(chunks[0]))
    elif len(chunks) == 4:
        return(str(chunks[3]) + thousands[3] + str(chunks[2]) + thousands[2] + 
                str(chunks[1]) + thousands[1] + str(chunks[0]))
    else:
        return("Number not in the range!")

def hundreds(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    c = n % 10 
    b = ((n % 100) - c) / 10 
    a = ((n % 1000) - (b * 10) - c) / 100
    t = "" 
    h = "" 
    if a != 0 and b == 0 and c == 0: 
        t = ones[a] + "hundred " 
    elif a != 0: 
        t = ones[a] + "hundred and "
    

def say(number):



