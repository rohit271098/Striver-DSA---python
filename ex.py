def repeatingElements(arr):
    n = len(arr)
    temp = []

    for i in range(n):
        if arr[i] == arr[i-1]:
            temp.append(arr[i])
    return temp

arr = [1,2,3,3]
print(repeatingElements(arr))
