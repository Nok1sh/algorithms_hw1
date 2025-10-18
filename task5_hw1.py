from test_alg import universal_test_system
from test_for_all_tasks import task5


def calculate(first_operand: float, operation: str, second_operand: int):
    print(f"DEBUG: calculate({first_operand}, '{operation}', {second_operand})")
    if operation == "+":
        return first_operand + second_operand
    elif operation == "-":
        return first_operand - second_operand
    raise ValueError


name, solutions, tests = task5()

solutions[name] = calculate

universal_test_system(solutions, tests)