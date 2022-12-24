a = input('введите числа через пробел: ')

b = int(input('введите любое число: '))

list_a = list(map(int, a.split()))

def sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]
    return print(array)

sort(array=list_a)

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array=sort(array=list_a), element=b-1,left=0, right=len(list_a) -1))

