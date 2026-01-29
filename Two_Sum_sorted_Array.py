numbers = [2, 3, 4]
target = 6
n = len(numbers) - 1
index1, index2 = 0, n
output = []

while index1 < index2:
    sum = numbers[index1] + numbers[index2]
    if sum == target:
        output = [index1 + 1, index2 + 1]
        break
    elif sum < target:
        index1 += 1
    else:
        index2 -= 1
print(output)
