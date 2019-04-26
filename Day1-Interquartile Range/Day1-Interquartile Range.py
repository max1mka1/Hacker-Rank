
def input_array():
    return list(map(int, input().split()))

def create_dataset():
    global n, X, F
    s = []
    for i in range(n):
        for j in range(F[i]):
            s.append(X[i])
    return s

def Q (x, A, B):
    global m
    m = A + (B - A)//2
    if ((B - A) % 2) == 0:
        return (x[m] + x[m - 1])/2
    else:
        return (x[m])

m = 0
n = int(input())
X = input_array()
F = input_array()
S = create_dataset()
N = sum(F)
S.sort()
print('S = ', S, '; N = ', N)
Q2 = Q(S, 0, N)
print('Q2 = ', Q2)
m2 = m
Q1 = Q(S, 0, m2)
print('Q1 = ', Q1)
if n%2 != 0:
    m2 += 1
Q3 = Q(S, m2, N)
print('Q3 = ', Q3)
print('Q3 - Q1 =  ', Q3 - Q1)
print(round(Q3 - Q1, 1))
