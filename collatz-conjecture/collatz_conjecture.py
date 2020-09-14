def steps(number):
    if number is not int:
            raise TypeError('Work with integers only')
    if number is int & number < 0:
            raise ValueError('WOrk with positive integers only')
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
    print("For input n = " + str(number_ini) + ", the return value would be " + str(n) )
    return(n)
    
    
steps(12)
steps(-3)
steps(0)