
def func():
    with open("test_30.txt", "r") as file:
        n = int(file.readline())
        intervals = []
        for ind in range(n):
            inter = file.readline().split()
            start, end = int(inter[0]), int(inter[1])
            intervals.append((start, end, ind+1))
        m = int(file.readline())
        points = []
        for _ in range(m):
            point = int(file.readline())
            points.append(point)
        
    result = []

    ind_intervals = 0

    for point in points:
        minlength = None
        ind_minlength = -1
        while ind_intervals < n:
            start = intervals[ind_intervals][0]
            if point < start:
                break
        
            end = intervals[ind_intervals][1]
            if point <= end:
                length = end - start
                if minlength is None:
                    minlength = length
                    ind_minlength = intervals[ind_intervals][2]
                elif minlength > length:
                    minlength = length
                    ind_minlength = intervals[ind_intervals][2]
            
            ind_intervals += 1

        result.append(ind_minlength)
    
    return result

        
print(func())
