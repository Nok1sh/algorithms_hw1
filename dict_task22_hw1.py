from tools.mergesort import MergeSort
from test_alg import universal_test_system
from test_for_all_tasks import task22


def func(filename):
    
    with open(filename, "r") as file:
        n = int(file.readline())

        name_city = {}
        name_money = {}
        city_money ={}
        city_best_days = {}

    
        for _ in range(n):
            name, city, amount = file.readline().split()
            amount = int(amount)

            name_money[name] = amount
            name_city[name] = city
            city_money[city] = city_money.get(city, 0) + amount
            city_best_days[city] = 0


        m, k = file.readline().split()
        m = int(m)
        k = int(k)

        move_days = []
        for _ in range(k):
            day, name, city = file.readline().split()
            move_days.append((int(day), name, city))

        move_days = MergeSort.merge(move_days)

    def id_richer_city():
        richest_name = 0 
        max_amount = -1
        for city, money in city_money.items():
            if money > max_amount or (money == max_amount and city < richest_name):
                max_amount = money
                richest_name = city
        return richest_name

    move_id = 0
    richest_city = id_richer_city()

    for day in range(1, m+1):

        while move_id < k and move_days[move_id][0] == day:
            name, new_city = move_days[move_id][1], move_days[move_id][2]
            old_city = name_city[name]
            amount = name_money[name]
            
            if old_city != new_city:
                city_money[old_city] -= amount
                
                city_money[new_city] = city_money.get(new_city, 0) + amount
                name_city[name] = new_city
                
                if new_city not in city_best_days:
                    city_best_days[new_city] = 0
            
            move_id += 1
        
        
        richest_city = id_richer_city()
        city_best_days[richest_city] += 1

    result_city = []
    for city, money in city_best_days.items():
        if money > 0:
            result_city.append((city, money)) 

    return MergeSort.merge(result_city)


name, solutions, tests = task22()

solutions[name] = func

universal_test_system(solutions, tests)