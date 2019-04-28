
def g(p, n):
    return (1 - p) ** (n - 1) * p

num, den = list(map(int, input().split()))
p =  num/den
n = int(input())
print(round(g(p, n), 3))
