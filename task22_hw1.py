from tools.mergesort import MergeSort
from test_alg import universal_test_system
from test_for_all_tasks import task22


def binary_search(array, value):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def func(filename):
    
    with open(filename, "r") as file:
        n = int(file.readline())

        names = []
        cities = []
        money = []

        all_cities = []
        money_in_cities = []

        flag_sort_cities = True
        days_best_city = []
    
        flag_found = True
        for _ in range(n):
            name, city, amount = file.readline().split()
            amount = int(amount)

            names.append(name)
            cities.append(city)
            money.append(amount)
            flag_found = False
            for i in range(len(all_cities)):
                if all_cities[i] == city:
                    money_in_cities[i] += amount
                    flag_found = True
                    break
            if not flag_found:
                all_cities.append(city)
                money_in_cities.append(amount)
                days_best_city.append(0)

        m, k = file.readline().split()
        m = int(m)
        k = int(k)

        move_day = []
        move_name = []
        move_city = []

        for _ in range(k):
            day, name, city = file.readline().split()
            move_day.append(int(day))
            move_name.append(name)
            move_city.append(city)

    day = 1
    moves = 0

    def id_richer_city():
        richest_idx = 0
        for i in range(1, len(all_cities)):
            if money_in_cities[i] > money_in_cities[richest_idx]:
                richest_idx = i
            elif money_in_cities[i] == money_in_cities[richest_idx] and all_cities[i] < all_cities[richest_idx]:
                richest_idx = i
        return richest_idx

    while day <= m:

        while moves < k and move_day[moves] == day:
            id_billioner = -1
            for i in range(len(names)):
                if names[i] == move_name[moves]:
                    id_billioner = i
                    break
            cur_city = cities[id_billioner]
            new_city = move_city[moves]
            amount = money[id_billioner]

            cur_city_id = -1
            for i in range(len(all_cities)):
                if all_cities[i] == cur_city:
                    cur_city_id = i
                    break

            new_city_id = -1
            for i in range(len(all_cities)):
                if all_cities[i] == new_city:
                    new_city_id = i
                    break
        
            if new_city_id == -1:
                all_cities.append(new_city)
                money_in_cities.append(0)
                days_best_city.append(0) 
                new_city_id = len(all_cities) - 1
            
            money_in_cities[cur_city_id] -= amount
            money_in_cities[new_city_id] += amount
            cities[id_billioner] = new_city

            moves += 1
        
        days_best_city[id_richer_city()] += 1
        day += 1

    result_city = []
    for i in range(len(days_best_city)):
        if days_best_city[i] != 0:
            result_city.append((all_cities[i], days_best_city[i]))

    
    return MergeSort.merge(result_city)


name, solutions, tests = task22()

solutions[name] = func

universal_test_system(solutions, tests)
