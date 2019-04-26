
def Q (x, A, B):
    global m
    if ((B - A) % 2) == 0:
        m = (A + (B - A)//2)
        return (x[A + (B - A)//2] + x[(A + (B - A)//2)-1])/2
    else:
        m = A + (B - A)//2
        return (x[A + (B - A)//2])

N = int(input())
X = list(map(int, input().split()))
X.sort()
#print("Sorted = { ", X, " }")
m = 0
q2 = Q (X, 0, N)
m2 = m
#print("m2 = { ", m2, " }")
q1 = Q(X, 0, m2)
if N%2 != 0:
    m2 += 1
q3 = Q (X, m2, N)
print(int(q1))
print(int(q2))
print(int(q3))
