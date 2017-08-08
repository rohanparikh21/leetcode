def peaks_and_valleys_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        i = 0
        j = 1
        while j < len(arr):
            if j % 2 == 0:
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
            else:
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
            i += 1
            j += 1
    return arr


if __name__ == '__main__':
    print peaks_and_valleys_sort([5,3,1,2,3])


