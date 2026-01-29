lst1 = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(lst1):
    diff = target - num
    if diff in seen:
        lst2 = (seen[diff], i)
    seen[num] = i

output = list(lst2)
print(output)
