import statistics as st

def input_array():
    return list(map(int, input().split()))

def create_dataset():
    global n, X, F
    s = []
    for i in range(n):
        for j in range(F[i]):
            s.append(X[i])
    return s

n = int(input())
X = input_array()
F = input_array()
N = sum(F)
S = create_dataset()
S.sort()

if n%2 != 0:
    Q1 = st.median(S[:N//2])
    Q3 = st.median(S[N//2+1:])
else:
    Q1 = st.median(S[:N//2])
    Q3 = st.median(S[N//2:])

print(round(float(Q3-Q1), 1))
