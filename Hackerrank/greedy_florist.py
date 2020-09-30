def getMinimumCost(k, c):
    n = len(c)
    x = n // k
    price = 0
    for i in range(1 , x + 1):
        for _ in range(k):
            max_c = max(c)
            price += max_c * i
            c.remove(max_c)
    for j in c:
        price += j * (i +  1)
    return price

print(getMinimumCost(3 , [2, 5 , 6]))
