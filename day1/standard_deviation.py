# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
X = list(map(int, input().strip().split()))

mean = sum(X) / n
tmp = sum([(x - mean)**2 for x in X])
ans = round(math.sqrt(tmp/n), 1)
print(ans)
