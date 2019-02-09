n = input()
first = sorted(map(int, raw_input().split()))
second = sorted(map(int, raw_input().split()))

final = 0
for i in range(n):
    final += (first[i]*second[i])

print(final)
