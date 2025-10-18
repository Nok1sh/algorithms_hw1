import random
import string

def task3():
    solutions = {
    "Связный список": None
    }

    tests = {
        "Связный список": [
            {"input": "1 2 6 8 7 3 0 4 1 6 2 3 9 0", "expected": [4, 7, 8, 9], "count": len("1 2 6 8 7 3 0 4 1 6 2 3 9 0".replace(" ", ""))},
            {"input": "10 20 30 0 40 50", "expected": [10, 20, 30, 40, 50], "count": len("10 20 30 0 40 50".replace(" ", ""))},
            {"input": "5 4 3 0 2 1", "expected": [1, 2, 3, 4, 5], "count": len("5 4 3 0 2 1".replace(" ", ""))},
            {"input": " ".join(map(str, range(1, 20001))) + " 0 " + " ".join(map(str, range(1000, 19001))) + " 0",
        "expected": list(range(1, 1000)) + list(range(19001, 20001)), "count": len("".join(map(str, range(1, 20001))) + " 0 " + "".join(map(str, range(1000, 19001))) + " 0")},
            {"input": " ".join(map(str, range(1, 10001))) + " 0 " + " ".join(map(str, range(10001, 20001))) + " 0",
            "expected": list(range(1, 20001)), "count": len("".join(map(str, range(1, 10001))) + " 0 " + "".join(map(str, range(10001, 20001))) + " 0")},
            {
        "input": " ".join(map(str, range(1, 20001))) + " 0 " + " ".join(map(str, range(2, 20000))) + " 0",
        "expected": [1, 20000],
        "count": len("".join(map(str, range(1, 20001))) + "0" + "".join(map(str, range(2, 20000))) + "0")
            },
            {
        "input": " ".join(map(str, range(1, 20001, 2))) + " 0 " + " ".join(map(str, range(2, 20001, 2))) + " 0",
        "expected": list(range(1, 20001)),
        "count": len("".join(map(str, range(1, 20001, 2))) + "0" + "".join(map(str, range(2, 20001, 2))) + "0")
            },
            {
        "input": " ".join(map(str, range(1, 20001))) + " 0 0",
        "expected": list(range(1, 20001)),
        "count": len("".join(map(str, range(1, 20001))) + "00")
        },
        {
        "input": "0 " + " ".join(map(str, range(1, 20001))) + " 0",
        "expected": list(range(1, 20001)),
        "count": len("0" + "".join(map(str, range(1, 20001))) + "0")
        },
        {
        "input": "1 20000 0 1 19999 0",
        "expected": [19999, 20000],
        "count": len("12000001199990")
        }

        ]}
    return "Связный список", solutions, tests

def task5():
    tests = {
    "Калькулятор": [
        {"input": [5, "+", 3], "expected": 8},
        {"input": [10, "-", 4], "expected": 6},
        {"input": [0, "+", 0], "expected": 0},
        {"input": [0, "-", 0], "expected": 0},
        {"input": [-5, "+", 3], "expected": -2},
        {"input": [5, "-", -3], "expected": 8},
        {"input": [-5, "-", -3], "expected": -2},
        {"input": [2147483647, "+", 1], "expected": 2147483648},
        {"input": [-2147483648, "-", 1], "expected": -2147483649},
        {"input": [10**10, "-", 9**12], "expected": 10**10 - 9**12},
        ]
    }

    solutions = {
        "Калькулятор": None
    }
    return "Калькулятор", solutions, tests

def task8():
    tests = {
        "Магараджа": [
            {"input": [3, 1], "expected": 9},
            {"input": [4, 2], "expected": 20},
            
            {"input": [1, 1], "expected": 1},
            {"input": [2, 1], "expected": 4},
            
            {"input": [3, 3], "expected": 0},  
            
            {"input": [5, 1], "expected": 25},
            {"input": [5, 5], "expected": 10}, 
            
            {"input": [3, 4], "expected": 0},
            {"input": [1, 2], "expected": 0},
            
            {"input": [10, 1], "expected": 100}    
        ]
    }

    solutions = {
        "Магараджа": None
    }
    return "Магараджа", solutions, tests

def task12():
    def generate_large_test_cases():
        nonlocal test_cases_quicksort
        
        def generate_random_name(length=10):
            return ''.join(random.choices(string.ascii_lowercase, k=length))
        
        large_tests = []
        
        participants_100 = []
        for i in range(100):
            name = generate_random_name(8)
            solved = random.randint(0, 100)
            penalty = random.randint(0, 1000)
            participants_100.append([name, solved, penalty])
        
        expected_100 = [p[0] for p in sorted(participants_100, 
                                            key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_100],
            "expected": expected_100
        })
        
        participants_500 = []
        for i in range(500):
            name = f"user_{i:03d}"
            solved = random.choice([0, 5, 10, 15, 20]) 
            penalty = random.randint(0, 500)
            participants_500.append([name, solved, penalty])
        
        expected_500 = [p[0] for p in sorted(participants_500, 
                                            key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_500],
            "expected": expected_500
        })
        
        participants_1000 = []
        for i in range(1000):
            name = generate_random_name(15)
            if i % 3 == 0:
                solved = 0
                penalty = 0
            elif i % 3 == 1:
                solved = 1000000000
                penalty = 1000000000
            else:
                solved = random.randint(1, 999999999)
                penalty = random.randint(1, 999999999)
            participants_1000.append([name, solved, penalty])
        
        expected_1000 = [p[0] for p in sorted(participants_1000, 
                                            key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_1000],
            "expected": expected_1000
        })
        
        participants_2000_same_p = []
        same_solved = 50
        for i in range(2000):
            name = generate_random_name(12)
            penalty = random.randint(0, 10000)
            participants_2000_same_p.append([name, same_solved, penalty])
        
        expected_2000_same_p = [p[0] for p in sorted(participants_2000_same_p, 
                                                    key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_2000_same_p],
            "expected": expected_2000_same_p
        })
        
        participants_1500_same_pf = []
        same_solved = 25
        same_penalty = 100
        for i in range(1500):
            name = generate_random_name(10)
            participants_1500_same_pf.append([name, same_solved, same_penalty])
        
        expected_1500_same_pf = [p[0] for p in sorted(participants_1500_same_pf, 
                                                    key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_1500_same_pf],
            "expected": expected_1500_same_pf
        })
        
        participants_3000_sequential = []
        for i in range(3000):
            name = f"participant_{i:04d}"
            solved = i % 100  
            penalty = i * 3
            participants_3000_sequential.append([name, solved, penalty])
        
        expected_3000_sequential = [p[0] for p in sorted(participants_3000_sequential, 
                                                        key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_3000_sequential],
            "expected": expected_3000_sequential
        })
        
        participants_2500_max_len = []
        for i in range(2500):
            name = generate_random_name(20)  
            solved = random.randint(0, 1000)
            penalty = random.randint(0, 10000)
            participants_2500_max_len.append([name, solved, penalty])
        
        expected_2500_max_len = [p[0] for p in sorted(participants_2500_max_len, 
                                                    key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_2500_max_len],
            "expected": expected_2500_max_len
        })
        
        participants_4000_special = []
        for i in range(4000):
            name = generate_random_name(8)
            if i < 1000:
                solved = random.randint(800, 1000)
            elif i < 2000:
                solved = random.randint(500, 799)
            elif i < 3000:
                solved = random.randint(200, 499)
            else:
                solved = random.randint(0, 199)
            penalty = random.randint(0, 5000)
            participants_4000_special.append([name, solved, penalty])
        
        expected_4000_special = [p[0] for p in sorted(participants_4000_special, 
                                                    key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_4000_special],
            "expected": expected_4000_special
        })
        
        participants_3500_pattern = []
        base_names = ["alex", "bob", "charlie", "diana", "eva", "frank", "grace", "henry"]
        for i in range(3500):
            base_name = random.choice(base_names)
            name = f"{base_name}_{i:04d}"
            solved = random.randint(0, 100)
            penalty = random.randint(0, 2000)
            participants_3500_pattern.append([name, solved, penalty])
        
        expected_3500_pattern = [p[0] for p in sorted(participants_3500_pattern, 
                                                    key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_3500_pattern],
            "expected": expected_3500_pattern
        })
        
        participants_5000_large = []
        for i in range(5000):
            name = generate_random_name(random.randint(5, 20))
            solved = random.randint(0, 1000000000)
            penalty = random.randint(0, 1000000000)
            participants_5000_large.append([name, solved, penalty])
        
        expected_5000_large = [p[0] for p in sorted(participants_5000_large, 
                                                key=lambda x: (-x[1], x[2], x[0]))]
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_5000_large],
            "expected": expected_5000_large
        })
        
        participants_extreme = []
        
        for i in range(100000):
            name = generate_random_name(20)
            
            solved = random.randint(0, 1000000000)
            penalty = random.randint(0, 1000000000)
            
            participants_extreme.append([name, solved, penalty])
        
        expected_extreme = [p[0] for p in sorted(participants_extreme, 
                                            key=lambda x: (-x[1], x[2], x[0]))]
        
        
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_extreme],
            "expected": expected_extreme
        })
        
        participants_stress = []
        
        for i in range(80000):
            if i % 4 == 0:
                name = 'x' * 20 
            elif i % 4 == 1:
                name = 'a' * 10 + 'z' * 10  
            elif i % 4 == 2:
                name = ''.join([chr(97 + (i + j) % 26) for j in range(20)]) 
            else:
                name = 'user_' + str(i).zfill(10) + '_end'  
            
            solved = 1000000000 if i % 3 == 0 else random.randint(0, 1000000000)
            penalty = 1000000000 if i % 5 == 0 else random.randint(0, 1000000000)
            
            participants_stress.append([name, solved, penalty])
            

        expected_stress = [p[0] for p in sorted(participants_stress, 
                                            key=lambda x: (-x[1], x[2], x[0]))]
        
        test_cases_quicksort["Быстрая сортировка"].append({
            "input": [participants_stress],
            "expected": expected_stress
        })

        

    test_cases_quicksort = {
        "Быстрая сортировка": [
            {
                "input": [[
                    ["alla", 4, 100],
                    ["gena", 6, 1000],
                    ["gosha", 2, 90],
                    ["rita", 2, 90],
                    ["timofey", 4, 80]
                ]],
                "expected": ["gena", "timofey", "alla", "gosha", "rita"]
            },
            {
                "input": [[
                    ["alla", 0, 0],
                    ["gena", 0, 0],
                    ["gosha", 0, 0],
                    ["rita", 0, 0],
                    ["timofey", 0, 0]
                ]],
                "expected": ["alla", "gena", "gosha", "rita", "timofey"]
            },
            
            
            {
                "input": [[["single", 10, 100]]],
                "expected": ["single"]
            },
            
            {
                "input": [[[f"user{i}", i % 100, i * 10] for i in range(1000)]],
                "expected": [f"user{i}" for i in sorted(range(1000), 
                            key=lambda x: (-(x % 100), x * 10, f"user{x}"))]
            },
            
            {
                "input": [[
                    ["a" * 20, 10, 100],
                    ["b" * 20, 10, 50],
                    ["c" * 20, 5, 0]
                ]],
                "expected": ["a" * 20, "b" * 20, "c" * 20]
            },
            
            {
                "input": [[
                    ["min_values", 0, 0],
                    ["max_values", 1000000000, 1000000000],
                    ["mixed", 500000000, 250000000]
                ]],
                "expected": ["max_values", "mixed", "min_values"]
            },
            
            {
                "input": [[
                    ["alice", 5, 100],
                    ["bob", 5, 50],
                    ["charlie", 5, 200],
                    ["dave", 5, 50]
                ]],
                "expected": ["bob", "dave", "alice", "charlie"]
            },
            
            {
                "input": [[
                    ["zeta", 3, 100],
                    ["alpha", 3, 100],
                    ["beta", 3, 100],
                    ["gamma", 3, 100]
                ]],
                "expected": ["alpha", "beta", "gamma", "zeta"]
            },
            
            {
                "input": [[
                    ["aaa", 5, 100],
                    ["bbb", 5, 100],
                    ["ccc", 5, 100],
                    ["ddd", 5, 100]
                ]],
                "expected": ["aaa", "bbb", "ccc", "ddd"]
            },
            
            {
                "input": [[
                    ["a", 5, 100],
                    ["aa", 5, 100],
                    ["aaa", 5, 100],
                    ["b", 5, 100]
                ]],
                "expected": ["a", "aa", "aaa", "b"]
            },
            
            {
                "input": [[
                    ["zero_solved", 0, 0],
                    ["max_solved", 1000000000, 1000000000],
                    ["one_solved", 1, 1]
                ]],
                "expected": ["max_solved", "one_solved", "zero_solved"]
            },
            
            {
                "input": [[
                    ["low_penalty", 10, 1],
                    ["high_penalty", 10, 999999999],
                    ["medium_penalty", 10, 500000000]
                ]],
                "expected": ["low_penalty", "medium_penalty", "high_penalty"]
            },
            
            {
                "input": [[
                    ["z_user", 5, 100],
                    ["a_user", 5, 100],
                    ["m_user", 5, 100]
                ]],
                "expected": ["a_user", "m_user", "z_user"]
            },
            
            {
                "input": [[
                    ["user1", 5, 50],
                    ["user2", 5, 50],
                    ["user3", 5, 100],
                    ["user4", 10, 50],
                    ["user5", 10, 100]
                ]],
                "expected": ["user4", "user5", "user1", "user2", "user3"]
            },
            
            {
                "input": [[
                    ["user_1", 5, 100],
                    ["user-2", 5, 100],
                    ["user.3", 5, 100]
                ]],
                "expected": ["user-2", "user.3", "user_1"]
            },
            
            {
                "input": [[
                    ["a", 5, 100],
                    ["b", 5, 100],
                    ["c", 5, 100],
                    ["d", 5, 100]
                ]],
                "expected": ["a", "b", "c", "d"]
            }
        ]
    }

    solutions = {
        "Быстрая сортировка": None
    }
    generate_large_test_cases()
    return "Быстрая сортировка", solutions, test_cases_quicksort

def task13():
    def generate_large_dataset(size=10000):
        arr = []
        for _ in range(size):
            score = random.randint(-100000, 100000)
            arr.append(score)
        return size, arr

    test_cases_max_triple = {
        "Максимальная тройка": [
            {"input": [10, [-1, 2, 3, -4, -2, 5, 1, 0, -3, 4]], "expected": 60},
            {"input": [5, [-1, 5, -3, -2, 4]], "expected": 30},
            
            {"input": [3, [1, 2, 3]], "expected": 6},
            {"input": [3, [-1, -2, -3]], "expected": -6},
            {"input": [3, [-1, -2, 3]], "expected": 6},
            {"input": [4, [0, 0, 0, 0]], "expected": 0},
            {"input": [5, [-1, -2, 0, 1, 2]], "expected": 4},
            
            {"input": [4, [1000000, 1000000, 1000000, 1000000]], "expected": 1000000000000000000},
            {"input": [4, [-1000000, -1000000, -1000000, -1000000]], "expected": -1000000000000000000},
            {"input": [5, [-1000000, -1000000, 1000000, 1000000, 1000000]], "expected": 1000000000000000000},
        ]
    }

    def generate_large_tests():
        large_tests = []
        
        n1 = 10000
        arr1 = [random.randint(-1000000, 1000000) for _ in range(n1)]
        sorted1 = sorted(arr1)
        expected1 = max(sorted1[-1] * sorted1[-2] * sorted1[-3], sorted1[0] * sorted1[1] * sorted1[-1])
        large_tests.append({"input": [n1, arr1], "expected": expected1})
        
        n2 = 50000
        arr2 = [random.randint(-1000000, 1000000) for _ in range(n2)]
        sorted2 = sorted(arr2)
        expected2 = max(sorted2[-1] * sorted2[-2] * sorted2[-3], sorted2[0] * sorted2[1] * sorted2[-1])
        large_tests.append({"input": [n2, arr2], "expected": expected2})
        
        n3 = 100000
        arr3 = [random.randint(-1000000, 1000000) for _ in range(n3)]
        sorted3 = sorted(arr3)
        expected3 = max(sorted3[-1] * sorted3[-2] * sorted3[-3], sorted3[0] * sorted3[1] * sorted3[-1])
        large_tests.append({"input": [n3, arr3], "expected": expected3})
        
        n4 = 500000
        arr4 = [random.randint(-1000000, 1000000) for _ in range(n4)]
        sorted4 = sorted(arr4)
        expected4 = max(sorted4[-1] * sorted4[-2] * sorted4[-3], sorted4[0] * sorted4[1] * sorted4[-1])
        large_tests.append({"input": [n4, arr4], "expected": expected4})
        
        n5 = 1000000
        arr5 = [random.randint(-1000000, 1000000) for _ in range(n5)]
        sorted5 = sorted(arr5)
        expected5 = max(sorted5[-1] * sorted5[-2] * sorted5[-3], sorted5[0] * sorted5[1] * sorted5[-1])
        large_tests.append({"input": [n5, arr5], "expected": expected5})
        
        return large_tests

    def generate_extreme_tests():
        extreme_tests = []
        
        n1 = 100000
        arr1 = [random.randint(1, 1000000) for _ in range(n1)]
        sorted1 = sorted(arr1)
        expected1 = sorted1[-1] * sorted1[-2] * sorted1[-3]
        extreme_tests.append({"input": [n1, arr1], "expected": expected1})
        
        n2 = 100000
        arr2 = [random.randint(-1000000, -1) for _ in range(n2)]
        sorted2 = sorted(arr2)
        expected2 = sorted2[-1] * sorted2[-2] * sorted2[-3]
        extreme_tests.append({"input": [n2, arr2], "expected": expected2})
        
        n3 = 10000
        arr3 = [-1000000, -999999, 999999, 1000000] + [random.randint(-100, 100) for _ in range(n3 - 4)]
        expected3 = (-1000000) * (-999999) * 1000000
        extreme_tests.append({"input": [n3, arr3], "expected": expected3})
        
        n4 = 100000
        arr4 = []
        for i in range(n4):
            if i % 2 == 0:
                arr4.append(1000000)
            else:
                arr4.append(-1000000)
        expected4 = 1000000 * 1000000 * 1000000
        extreme_tests.append({"input": [n4, arr4], "expected": expected4})
        
        return extreme_tests

    large_tests = generate_large_tests()
    extreme_tests = generate_extreme_tests()
    test_cases_max_triple["Максимальная тройка"].extend(large_tests)
    test_cases_max_triple["Максимальная тройка"].extend(extreme_tests)

    solutions = {
        "Максимальная тройка": None
    }
    return "Максимальная тройка", solutions, test_cases_max_triple


def task17():
    # func("test.txt")
    ind = 1
    count_files = 7
    test_cases = {"s":[]}
    solutions = {
        "s": None
    }

    for i in range(1, 8):
        path = f"tests_task17/{i}.txt"
        case_ = {"input": path, "expected": None}
        test_cases["s"].append(case_)

    # letters = string.ascii_letters
    # with open("tests_task17/7.txt", "w") as file:
    #     file.write("\n".join("".join(random.choices(letters, k=100000)) for i in range(10000)))
    return "s", solutions, test_cases, ind, count_files


def task19():
    test_cases_guards = {
        "Охранники": [
            {
                "input": [[2, 3, 0, 3000, 2500, 7000, 2700, 10000, 2, 0, 3000, 2700, 10000]],
                "expected": ["Wrong Answer", "Accepted"]
            },
            
            {
                "input": [[1, 1, 0, 10000]],  
                "expected": ["Accepted"]
            },
            {
                "input": [[1, 0]],  
                "expected": ["Wrong Answer"]
            },
            
            {
                "input": [[1, 3, 0, 4000, 3000, 7000, 6000, 10000]], 
                "expected": ["Accepted"]
            },
            {
                "input": [[1, 3, 0, 5000, 0, 5000, 5000, 10000]],  
                "expected": ["Wrong Answer"]
            },
        ]
    }

    def generate_large_guard_tests():
        
        large_tests = []
        
        test_data = [1, 100] 
        for i in range(100):
            start = i * 100
            end = start + 101  
            test_data.extend([start, end])
        
        large_tests.append({
            "input": [test_data],
            "expected": ["Accepted"]
        })
        
        test_data = [1, 500]
        for i in range(500):
            start = random.randint(0, 9900)
            end = random.randint(start + 1, 10000)
            test_data.extend([start, end])
        
        large_tests.append({
            "input": [test_data],
            "expected": ["Wrong Answer"]  
        })
        
        test_data = [30]
        for k in range(30):
            n_guards = 50
            test_data.append(n_guards)
            for i in range(n_guards):
                start = random.randint(0, 9900)
                end = random.randint(start + 1, 10000)
                test_data.extend([start, end])
        
        large_tests.append({
            "input": [test_data],
            "expected": ["Wrong Answer"] * 30
        })
        
        return large_tests

    def generate_extreme_guard_tests():
        
        extreme_tests = []
        
        test_data = [1, 10000]
        for i in range(10000):
            start = random.randint(0, 9999)
            end = random.randint(start + 1, 10000)
            test_data.extend([start, end])
        
        extreme_tests.append({
            "input": [test_data],
            "expected": ["Wrong Answer"]
        })
        
        test_data = [1, 100]
        for i in range(100):
            test_data.extend([0, 10000])
        
        extreme_tests.append({
            "input": [test_data],
            "expected": ["Wrong Answer"] 
        })
        
        test_data = [1, 100]
        for i in range(100):
            start = i * 100
            end = (i + 1) * 100
            test_data.extend([start, end])
        
        extreme_tests.append({
            "input": [test_data],
            "expected": ["Wrong Answer"] 
        })
        
        
        return extreme_tests


    large_tests = generate_large_guard_tests()
    test_cases_guards["Охранники"].extend(large_tests)

    extreme_tests = generate_extreme_guard_tests()
    test_cases_guards["Охранники"].extend(extreme_tests)

    solution = {
        "Охранники": None
    }
    return "Охранники", solution, test_cases_guards


def task22():
    test_cases = {"Billioners":[]}
    solutions = {
        "Billioners": None
    }
    results = []
    with open("tests_task22/results.txt", "r") as res:
        for i in res:
            results.append(eval(i))

    for i in range(1, len(results)+1):
        path = f"tests_task22/{i}.txt"
        case_ = {"input": path, "expected": results[i-1]}
        test_cases["Billioners"].append(case_)
    return "Billioners", solutions, test_cases


def task25():

    test_cases = {"heap":[]}
    solutions = {
        "heap": None
    }
    results = []
    with open("tests_task25/results.txt", "r") as res:
        for i in res:
            results.append(i)

    for i in range(1, len(results)+1):
        path = f"tests_task25/{i}.txt"
        case_ = {"input": path, "expected": results[i-1]}
        test_cases["heap"].append(case_)
    
    return "heap", solutions, test_cases


def task30():
    test_cases = {"intervals":[]}
    solutions = {
        "intervals": None
    }
    results = []
    with open("tests_task30/results.txt", "r") as res:
        for i in res:
            results.append(i)

    for i in range(1, len(results)+1):
        path = f"tests_task30/{i}.txt"
        case_ = {"input": path, "expected": results[i-1]}
        test_cases["intervals"].append(case_)
    return "intervals", solutions, test_cases