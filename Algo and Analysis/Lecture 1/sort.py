



def insertion_sort(arr):
    for i in range(len(arr)):
        arrI = arr[i]

        swapWith = -1
        for j in range(i - 1, 0, -1):
            arrJ = arr[j]
            if arrI < arrJ:
                swapWith = j 
            else:
                break

        if swapWith != -1:
            temp = arr[swapWith]
            arr[swapWith] = arr[i]
            arr[i] = temp

if __name__ == "__main__":
    arr = [1, 3, 2, 4]
    insertion_sort(arr)
    print(arr)
    pass
