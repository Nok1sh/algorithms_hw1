from test_alg import universal_test_system
from test_for_all_tasks import task12


def checkdifference(arr, pivot):

    if arr[1] != pivot[1]:
        return arr[1] > pivot[1]

    if arr[2] != pivot[2]:
        return arr[2] < pivot[2]
    
    return arr[0].lower() < pivot[0].lower()


def quicksort(left, right, arr):

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
    
    quicksort(left, j, arr)
    quicksort(i, right, arr)


def func(arr):
    quicksort(0, len(arr)-1, arr)
    new_arr = []
    for pers in arr:
        new_arr.append(pers)
    return new_arr


name, solutions, tests = task12()

solutions[name] = func

universal_test_system(solutions, tests)
