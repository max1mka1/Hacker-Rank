
def fact(n):
    if n > 1:
        return n*fact(n - 1)
    else:
        return 1

def comb(n, r):
    return fact(n)/(fact(r)*fact(n - r))

def binom(p, n, rej):
    sum = 0
    for i in range(rej, n + 1):
        sum += comb(n, i) * p ** i * (1 - p) ** (n - i)
    return sum

def binom2(p, n):
    sum = 0
    for i in range(0, 3):
        sum += comb(n, i) * p ** i * (1 - p) ** (n - i)
    return sum

bad_percent, batch = list(map(int, input().split()))
good_percent = 100 - bad_percent
p =  bad_percent/(bad_percent + good_percent)
print(round(binom2(p, batch), 3))
print(round(binom(p, batch, 2), 3))
