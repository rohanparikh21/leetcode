def find_local_maxima(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = (0 + len(arr))/2
        prev = arr[mid - 1] if (mid - 1) >= 0 else None
        if prev and prev<arr[mid]:
            pass
        else:
            return find_local_maxima(arr[:mid])

        next = arr[mid + 1] if (mid + 1) < len(arr) else None
        if not next or next<arr[mid]:
            return arr[mid]
        else:
            return find_local_maxima(arr[mid+1:])


if __name__ == '__main__':
    print find_local_maxima([11,10,9,8,7,6,5,4,3,2,1])