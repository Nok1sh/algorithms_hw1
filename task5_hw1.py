from test_alg import universal_test_system
from test_for_all_tasks import task5

def calculate(first_operand: int, operation: str, second_operand: int) -> str:

    if operation == "+":
        first_operand = str(first_operand)
        second_operand = str(second_operand)

        first_negative = True if first_operand[0] == "-" else False
        second_neganive = True if second_operand[0] == "-" else False

        first_operand = first_operand[1:] if first_negative else first_operand
        second_operand = second_operand[1:] if second_neganive else second_operand
    
        if first_negative == second_neganive:

            i, j = len(first_operand) - 1, len(second_operand) - 1
            carry = 0
            result_digits = []

            while i >= 0 or j >= 0 or carry:
                first_digit = int(first_operand[i]) if i >= 0 else 0
                second_digit = int(second_operand[j]) if j >= 0 else 0
                total = first_digit + second_digit + carry
                carry = total // 10
                result_digits.append(str(total % 10))
                i -= 1
                j -= 1
            result_number = ""
            for digit in range(len(result_digits)-1, -1, -1):
                result_number += result_digits[digit]

            return ('-' + result_number) if first_negative else result_number

        else:
            if  first_operand >= second_operand:
                larger, smaller = first_operand, second_operand
                is_negative = first_negative
            else:
                larger, smaller = second_operand, first_operand
                is_negative = second_neganive

            i, j = len(larger) - 1, len(smaller) - 1
            borrow = 0
            result_digits = []
            while i >= 0:
                first_digit = int(larger[i]) - borrow
                second_digit = int(smaller[j]) if j >= 0 else 0
                borrow = 0
                if first_digit < second_digit:
                    first_digit += 10
                    borrow = 1
                result_digits.append(str(first_digit - second_digit))
                i -= 1
                j -= 1

            result_number = ""
            for digit in range(len(result_digits)-1, -1, -1):
                result_number += result_digits[digit]

            return ('-' + result_number) if is_negative else result_number


    if operation == "-":

        new_second_operand = -second_operand
        return calculate(first_operand, "+", new_second_operand)

    raise ValueError()

name, solutions, tests = task5()

solutions[name] = calculate

universal_test_system(solutions, tests)
