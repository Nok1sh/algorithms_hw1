

def check_heap():
    with open("test_25.txt", "r") as file:
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

print(check_heap())
