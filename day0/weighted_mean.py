# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    W = list(map(int, input().split()))

    weighted_mean = round(float(sum([x * w for x, w in zip(X, W)])) / sum(W), 1)
    print(weighted_mean)
