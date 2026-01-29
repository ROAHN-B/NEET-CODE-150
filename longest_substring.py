s = "abcabcbb"
max_len = 0
if len(s) == 0:
    print(0)
elif len(s) == 1:
    print(s[0])
else:
    substring = set()
    l = 0
    for r in range(len(s)):
        while s[r] in substring:
            substring.remove(s[l])
            l += 1
        substring.add(s[r])
        max_len = max(max_len, r - l + 1)
print(max_len)
