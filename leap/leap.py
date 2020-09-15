def leap_year(year):
     if year%4 == 0:
        if year%100 ==0:
            if year%400 == 0:
                return(str(year) +  " is a leap year")
            return(str(year) +  " is not a leap year")
        return(str(year) +  " is a leap year")

     else:
         return(str(year) + " is not a leap year")

print(leap_year(1999))
print(leap_year(2000))
print(leap_year(1900))
print(leap_year(2004))
