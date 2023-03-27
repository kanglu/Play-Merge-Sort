class MergeSort:
    """
    This is a class that will perform merge sort using an indirect array reference, that will leave the original data untouched.
    """

    def __init__(self, arr):
        self.length = len(arr)
        self.arr = arr

        # Create an indirect array so that we can leave the original array intact.
        self.iarr = []
        for i in range(self.length):
            self.iarr.append(i)

    def sort(self):
        self.merge_sort(0, self.length)
        print("====>Final Results:<====")
        for idx in self.iarr:
            print(self.arr[idx])

    def merge_sort(self, begin, end):
        if end - begin <= 1:
            return

        mid = (end + begin) // 2

        self.merge_sort(begin, mid)
        self.merge_sort(mid, end)

        return self.merge(begin, mid, end)

    def merge(self, begin, mid, end):
        i = 0
        j = 0

        leftLen = mid - begin
        rightLen = end - mid

        orig = self.iarr[begin:end]

        repl = 0
        while i < leftLen and j < rightLen:
            repl = begin + i + j
            if self.arr[orig[i]] < self.arr[orig[mid - begin + j]]:
                self.iarr[repl] = orig[i]
                i += 1
            else:
                self.iarr[repl] = orig[mid - begin + j]
                j += 1

        repl = begin + i + j
        for k in range(i, (mid - begin)):
            self.iarr[repl] = orig[k]
            repl += 1
        for k in range(j, (end - mid)):
            self.iarr[repl] = orig[mid - begin + k]
            repl += 1


if __name__ == "__main__":
    # Get a test array of strings from standard input
    #
    # cat names.txt | python ms.py
    #
    arr = []
    while True:
        try:
            s = input()
            arr.append(s)
        except EOFError:
            break

    sorter = MergeSort(arr)
    sorter.sort()
