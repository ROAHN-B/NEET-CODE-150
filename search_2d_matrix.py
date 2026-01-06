matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10


def binary_search(matrix, target):
    for ele in matrix:
        if ele[0] <= target <= ele[-1]:
            l, r = 0, len(ele) - 1
            while l <= r:
                mid = (l + r) // 2
                if ele[mid] == target:
                    return True
                elif ele[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

    return False


print(binary_search(matrix, target))
