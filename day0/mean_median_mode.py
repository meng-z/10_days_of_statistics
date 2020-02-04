# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))

    mean = round(float(sum(X)) / N, 1)
    print(mean)

    sorted_X = sorted(X)
    if N % 2 != 0:
        median = round(sorted_X[N // 2], 1)
    else:
        median = round(float(sorted_X[N // 2 - 1] + sorted_X[N // 2]) / 2, 1)
    print(median)

    c = Counter(sorted_X)
    mode = c.most_common(1)[0][0]
    print(mode)
