# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(int, input().strip().split()))
F = list(map(int, input().strip().split()))

X_F = {x:f for x, f in zip(X, F)}
sorted_X_F = sorted(X_F.items(), key=lambda x:x[0])
data = []
for t in sorted_X_F:
    data += ([t[0]]*t[1])


def median(ar, length):
    if length % 2 == 0:
        median = (ar[length // 2 - 1] + ar[length // 2]) / 2
    else:
        median = ar[length // 2]
    return float(median)

mid_idx = len(data) // 2
if n % 2 == 0:
    left = data[:mid_idx]
    right = data[mid_idx:]
else:
    left = data[:mid_idx]
    right = data[mid_idx + 1:] 

q1 = median(left, len(left))
q3 = median(right, len(right))
ans = round(q3 - q1, 1)
print(ans)
