def bs(arr, elem):
    if len(arr) == 0:
        return False
    mid = (0 + len(arr))/2
    if arr[mid] == elem:
        return True
    elif arr[mid] > elem:
        return bs(arr[:mid], elem)
    else:
        return bs(arr[mid+1:], elem)


if __name__ == '__main__':
    print bs([1,2,3,4,5], 1)
