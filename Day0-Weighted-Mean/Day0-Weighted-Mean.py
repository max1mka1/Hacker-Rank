
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def mean_weighted (x, w, n):
    p = 0
    sum_w = 0
    for i in range (n):
        p += x[i]*w[i]
        sum_w += w[i]
    return toFixed(p/sum_w, 1)
-
N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
print(mean_weighted (X, W, N))
