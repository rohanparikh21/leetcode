def quick_sort(arr):
    index = partition(arr)
    arr_left = []
    arr_right = []
    if index != 0:
        arr_left = quick_sort(arr[:index])
    if index != len(arr)-1:
        arr_right = quick_sort(arr[index+1:])
    return arr_left + [arr[index]] + arr_right


def partition(arr):
    print arr
    p = arr[0]
    i = 0
    j = 0
    for elem in arr[1:]:
        if elem < p:
            i += 1
            j += 1
            if i != j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        else:
            j += 1
    temp = arr[0]
    arr[0] = arr[i]
    arr[i] = temp
    return i

if __name__ == '__main__':
    print quick_sort([1,2,3,4,5])






