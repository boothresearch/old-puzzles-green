def score(x, y):
    if x**2 + y**2 <= 1:
        return("The point you earned is 10")
    elif x**2 + y**2 <= 5**2:
        return("The point you earned is 5")
    elif x**2 + y**2 <= 10**2:
        return("The point you earned is 1")
    else:
        return("The point you earned is 0")


print("If the point in the target is (0, 0) then you earn " + score(0, 0))
print("If the point in the target is (1, 0) then you earn " + score(1, 0))
print("If the point in the target is (5, 0) then you earn " + score(5, 0))
print("If the point in the target is (10, 0) then you earn " + score(10, 0))
print("If the point in the target is (14, 0) then you earn " + score(14, 0))