
import random

def high_of_three_in_array(array):

    high_element = max(array[0], array[1])
    low_element = min(array[0], array[1])

    high_of_two = high_element * low_element
    low_of_two = high_element * low_element

    high_of_three = array[0] * array[1] * array[2]

    for element in array[2:]:
        high_of_three = max(high_of_three, high_of_two * element, low_of_two*element)

        high_of_two = max(high_of_two, high_element*element, low_element * element)
        low_of_two = min(high_of_two, high_element*element, low_element * element)

        high_element = max(high_element, element)
        low_element = min(low_element, element)
    
    return high_of_three


def generate_large_dataset(size=10000):
    arr = []
    for _ in range(size):
        score = random.randint(-100000, 100000)
        arr.append(score)
    return arr

# array = [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2]
array = generate_large_dataset()
print(high_of_three_in_array(array))