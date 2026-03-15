A, B = map(int, input().split())
N = list(map(int, input().split()))
for n in N:
    if n < B:
        print(n, end = ' ')