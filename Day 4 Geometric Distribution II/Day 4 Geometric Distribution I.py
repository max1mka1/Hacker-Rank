
def g(p, n):
    sum = 0
    for i in range(1, n + 1):
        sum += (1 - p) ** (n - i) * p
    return sum

num, den = list(map(int, input().split()))
p =  num/den
n = int(input())
print(round(g(p, 5), 3))
