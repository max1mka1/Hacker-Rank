
def fact(n):
    if n > 1:
        return n*fact(n - 1)
    else:
        return 1

def combinations(r, n):
    return fact(n) / (fact(r) * fact(n - r))

def binom(boys, girls, x, n):
    p = boys/(boys + girls)
    #print('p = ', p)
    #print('q = ', q)
    #print('comb = ', combinations(x, n))
    #print('p**x = ', p**x)
    #print('q**(n - x) = ', q**(n - x))
    sum = 0
    for i in range(x, n + 1):
        sum += combinations(i, n) * p**i * (1 - p)**(n - i)
    return sum

boys, girls = list(map(float, input().split()))
b = binom(boys, girls, 3, 6)
print(round(b, 3))
