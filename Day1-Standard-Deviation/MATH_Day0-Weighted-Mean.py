
import math

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def mean(x, n):
    sum = 0
    for i in range (n):
        sum += x[i]
    return sum/n


def std_deviation (x, m):
    sum = 0
    for i in range (N):
        sum += math.pow(x[i] - m, 2)
    return toFixed(math.sqrt(sum/N), 1)


N = int(input())
X = list(map(int, input().split()))
m = mean(X, N)
print(std_deviation(X, m))
