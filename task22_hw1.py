from tools.mergesort import MergeSort


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

def func():
    
    with open("test_22.txt", "r") as file:
        n = int(file.readline())

        names_bil = []
        cities_bil = []
        money_bil = []

        all_cities = []
        money_in_cities = []

        flag_sort_cities = True

        for _ in range(n):
            name, city, amount = file.readline().split()
            amount = int(amount)

            names_bil.append(name)
            cities_bil.append(city)
            money_bil.append(amount)
            if flag_sort_cities:
                all_cities = MergeSort.merge(all_cities)
                flag_sort_cities = False

            city_index = binary_search(all_cities, city)
            if city_index != -1:
                money_in_cities[city_index] += amount
            
            else:
                all_cities.append(city)
                money_in_cities.append(amount)
                flag_sort_cities = True

        m, k = file.readline().split()
        m = int(m)
        k = int(k)

        move_day = []
        move_bil = []
        move_city = []

        for _ in range(k):
            day, name, city = file.readline().split()
            move_day.append(int(day))
            move_bil.append(name)
            move_city.append(city)
    
    days_best_city = [0]
    for _ in range(len(all_cities)):
        days_best_city.append(0)

    day = 1
    moves = 0
    flag_sort_cities = True

    def id_richer_city():
        max_amount = money_in_cities[0]
        richest_city = 0
        for i in range(1, len(all_cities)):
            if money_in_cities[i] > max_amount or (money_in_cities[i] == max_amount and all_cities[i] < all_cities[richest_city]):
                max_amount = money_in_cities[i]
                richest_city = i
        return richest_city

    while day <= m:

        while moves < k and move_day[moves] == day - 1:
            id_billioner = binary_search(names_bil, move_bil[moves]) 
            cur_city = cities_bil[id_billioner]
            new_city = move_city[moves]
            amount = money_bil[id_billioner]

            if flag_sort_cities:
                all_cities = MergeSort.merge(all_cities)
                flag_sort_cities = False
            
            cur_city_id = binary_search(all_cities, cur_city)
            new_city_id = binary_search(all_cities, new_city)
            if new_city_id == -1:
                all_cities.append(new_city)
                flag_sort_cities = True
                money_in_cities.append(0)
                days_best_city.append(0) 
                new_city_id = len(all_cities) - 1
            
            money_in_cities[cur_city_id] -= amount
            money_in_cities[new_city_id] += amount
            cities_bil[id_billioner] = new_city

            moves += 1
        
        days_best_city[id_richer_city()] += 1
        day += 1

    result_city = []
    for i in range(len(days_best_city)):
        if days_best_city[i] != 0:
            result_city.append(all_cities[i])

    result_city = MergeSort.merge(result_city)
    
    result = []
    for city in result_city:
        id_city = binary_search(all_cities, city)
        result.append((city, days_best_city[id_city]))
    
    return result

print(func())