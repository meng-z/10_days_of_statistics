# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(int, input().rstrip().split()))
sorted_X = sorted(X)

def median(ar, length):
    if length % 2 == 0:
        median = (ar[length // 2 - 1] + ar[length // 2]) / 2
    else:
        median = ar[length // 2]
    return int(median)

mid_idx = n // 2
if n % 2 == 0:
    left = sorted_X[:mid_idx]
    right = sorted_X[mid_idx:]
else:
    left = sorted_X[:mid_idx]
    right = sorted_X[mid_idx + 1:] 

q1 = median(left, len(left))
q2 = median(sorted_X, n)
q3 = median(right, len(right))
print(q1)
print(q2)
print(q3)
