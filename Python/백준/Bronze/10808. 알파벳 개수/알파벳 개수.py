S = input()
for i in range(26):
    count = 0
    a = chr(i + ord('a'))
    for ch in S:
        if ch == a:
            count += 1
    print(count, end = ' ')