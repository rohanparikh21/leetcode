def merge(arr1, arr2):
    print arr1, arr2
    aux_arr = []
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            aux_arr.append(arr1[i])
            i += 1
        else:
            aux_arr.append(arr2[j])
            j += 1

    if i<len(arr1):
        aux_arr.extend(arr1[i:])
    elif j<len(arr2):
        aux_arr.extend(arr2[j:])
    return aux_arr

def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:      # base case
        return arr
    else:
        mid = (0 + len(arr))/2
        arr1 = merge_sort(arr[:mid])
        arr2 = merge_sort(arr[mid:])
        return merge(arr1, arr2)

if __name__ == '__main__':
    import random
    print merge_sort(r)