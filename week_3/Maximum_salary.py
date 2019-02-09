def comp(n):
    res = ""
    while len(n) != 0:
        max_digit = '0'
        for number in n:
            if number + max_digit > max_digit + number:
                max_digit = number
        res += max_digit
        n.remove(max_digit)
    return res

m=input()
n = map(str,raw_input().split())
print(comp(n))
