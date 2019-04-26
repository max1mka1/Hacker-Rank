# Enter your code here. Read input from STDIN. Print output to STDOUT


def _input():
    for i in range (N):
        A[i] = int(input())

def mean(A):
    sum = 0
    for i in range (N):
        sum += A[i]
    return sum/N

def median(A):
    if (N % 2) == 0:
        return (A[N//2] + A[N//2-1])/2
    else:
        return (A[N//2])

def mode(A):
    max_num = 1
    t = 1
    max_id = 0
    for i in range (N):
        for j in range (N):
            if (j == i):
                continue
            if A[j] == A[i]:
                t += 1
        if (t > max_num):
            max_num = t
            max_id = i
    if (max_num > 1):
        return A[max_id]
    else:
        return A[0]

#size = int(input())
#numbers = list(map(int, input().split()))
#print(np.mean(numbers))
#print(np.median(numbers))

N = int(input())
A = [int(x) for x in input().split()]
A.sort()
print(mean(A))
print(median(A))
print(int(stats.mode(A)[0]))
