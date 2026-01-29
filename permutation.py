s1 = "abc"
s2 = "lecaabee"
found = False
for i in range(len(s2) - len(s1) + 1):
    substring = s2[i : i + len(s1)]
    if sorted(substring) == sorted(s1):
        found = True
        print(found)
        break
if not found:
    print(found)
