
def checkdifference(arr, pivot):

    if arr[1] != pivot[1]:
        return arr[1] > pivot[1]

    if arr[2] != pivot[2]:
        return arr[2] < pivot[2]
    
    return arr[0].lower() < pivot[0].lower()


def quicksort(left, right):
    global arr

    if left >= right:
        return
    
    i = left
    j = right

    pivot = arr[(left + right) // 2]

    while i <= j:
        while checkdifference(arr[i], pivot):
            i += 1
        while checkdifference(pivot, arr[j]):
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1      
    
    quicksort(left, j)
    quicksort(i, right)


# test 1

arr = [
    ("alla", 4, 100),
    ("gena", 6, 1000),
    ("gosha", 2, 90),
    ("rita", 2, 90),
    ("Timofey", 4, 80)
]
quicksort(0, len(arr)-1)
print(arr)

# test 2

arr = [
    ("alla", 0, 0),
    ("gena", 0, 0),
    ("gosha", 0, 0),
    ("rita", 0, 0),
    ("Timofey", 0, 0)
]
quicksort(0, len(arr)-1)
print(arr)