from test_alg import universal_test_system
from test_for_all_tasks import task13


def high_of_three_in_array(n, array):

    high_element = max(array[0], array[1])
    low_element = min(array[0], array[1])

    high_of_two = high_element * low_element
    low_of_two = high_element * low_element

    high_of_three = array[0] * array[1] * array[2]

    for element in range(2, n):
        high_of_three = max(high_of_three, high_of_two * array[element], low_of_two*array[element])

        high_of_two = max(high_of_two, high_element*array[element], low_element * array[element])
        low_of_two = min(high_of_two, high_element*array[element], low_element * array[element])

        high_element = max(high_element, array[element])
        low_element = min(low_element, array[element])
    
    return high_of_three

name, solutions, tests = task13()

solutions[name] = high_of_three_in_array

universal_test_system(solutions, tests)
