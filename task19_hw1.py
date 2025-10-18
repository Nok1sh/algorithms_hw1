from tools.mergesort import MergeSort
from test_alg import universal_test_system
from test_for_all_tasks import task19


def check_all_interval(intervals):
    intervals = MergeSort.merge(intervals)
    end = 0
    for a, b in intervals:
        if a > end:
            return False
        end = max(end, b)
    del intervals
    return end == 10000


def func(data):
    
    
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

    return results


name, solution, tests = task19()

solution[name] = func

universal_test_system(solution, tests)