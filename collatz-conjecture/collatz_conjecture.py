def steps(number):
    n = 0
    number_ini = number
    print(n, number)
 
    while (number != 1):
        if number % 2 == 0:
            number = int(number / 2)
            n = n + 1
            print(n, number)
        else:
            number = int(number*3 + 1)
            n = n + 1
            print(n, number)

    return("For input n = " + str(number_ini) + ", the return value would be " + str(n) )
    
    
steps(12)

