def TwoSum(arr, target):
    n = len(arr)

    if target in arr:
        return arr.index(target)
    else:
        for i in range(n):
            for j in range(i,n-1):
                if (arr[i] + arr[j+1]) == target:
                    return i,j+1


arr = [2,7,11,15]
target = 22
print(TwoSum(arr, target))

