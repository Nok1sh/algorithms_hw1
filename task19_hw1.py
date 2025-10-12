from tools.mergesort import MergeSort

def check_all_interval(intervals):
    intervals = MergeSort.merge(intervals)
    end = 0
    for a, b in intervals:
        if a > end:
            return False
        end = max(end, b)
    del intervals
    return end == 10000


def func():
    with open('test_19.txt', 'r') as file:
        data = []
        for i in file.read().split():
            data.append(int(i))
    
    k = data[0]
    index = 1
    results = []
    
    for _ in range(k):
        n = data[index]
        index += 1
        intervals = []
        for _ in range(n):
            a, b = data[index], data[index + 1]
            index += 2
            intervals.append((a, b))
        
        if not check_all_interval(intervals):
            results.append("Wrong Answer")
            continue
        
        status = "Accepted"
        for i in range(n):
            tmp = intervals[:i] + intervals[i+1:]
            if check_all_interval(tmp):
                status = "Wrong Answer"
                break
            del tmp
        
        results.append(status)

    with open('result_19.txt', 'w') as file:
        for i in range(len(results)-1):
            if "\n" in results[i]:
                file.write(results[i])
            else:
                file.write(results[i] + "\n")
        file.write(results[-1])
        del results, data

func()
