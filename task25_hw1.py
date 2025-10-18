from test_alg import universal_test_system
from test_for_all_tasks import task25

def check_heap(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        data = file.readline().split()
        heap = [0]
        for i in data:
            heap.append(int(i))

    for i in range(1, n + 1):
        if 2*i <= n and heap[i] > heap[2*i]:
            return "NO"
        if 2*i + 1 <= n and heap[i] > heap[2*i + 1]:
            return "NO"
    
    return "YES"

name, solutions, tests = task25()

solutions[name] = check_heap

universal_test_system(solutions, tests)