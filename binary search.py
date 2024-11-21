def binary_search(a, value):
    a.sort()
    if len(a) == 0:
            return False

    mid_index = len(a) // 2
    mid = a[mid_index]
    if value == mid:
        return True
    elif value < mid:
        return binary_search(a[:mid_index], value)
    else:
        return binary_search(a[mid_index + 1:], value)

a = [4, 55, 754, 5, 755, 5, 56625, 45, 7, 78]
g = binary_search(a, 5)
print(g)
