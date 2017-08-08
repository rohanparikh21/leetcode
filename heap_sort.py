class Heap(object):

    def __init__(self):
        self.heap_arr = []      # stores the heap data structure

    @staticmethod
    def __swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

    def insert(self, x):
        self.heap_arr.append(x)
        i = len(self.heap_arr)-1
        j = (i+1)/2 - 1
        while self.heap_arr[i] < self.heap_arr[j] and i >= 0 and j >= 0:
            self.heap_arr = self.__swap(self.heap_arr, i, j)
            i = j
            j = (i+1)/2 - 1

    def pop(self):
        return self.delete(0)

    def delete(self, idx):
        elem = self.heap_arr[idx]
        self.__swap(self.heap_arr, idx, len(self.heap_arr)-1)
        self.heap_arr = self.heap_arr[:-1]

        while True:
            i = 2 * idx + 1
            j = 2 * idx + 2
            smallest = idx
            if i < len(self.heap_arr) and self.heap_arr[idx] > self.heap_arr[i]:
                smallest = i

            if j < len(self.heap_arr) and self.heap_arr[smallest] > self.heap_arr[j]:
                smallest = j

            if smallest != idx:
                self.__swap(self.heap_arr, idx, smallest)
            else:
                break

        return elem


if __name__ == '__main__':
    h = Heap()
    arr1 = [5,4,3,2,1]
    for elem in arr1:
        h.insert(elem)

    for i in range(len(arr1)):
        print h.pop()


