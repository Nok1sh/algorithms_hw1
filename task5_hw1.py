
def calculate(first_operand: float, operation: str, second_operand: int):
    if operation == "+":
        return first_operand + second_operand
    elif operation == "-":
        return first_operand - second_operand
    raise ValueError

# 1 test

first_operand = 123
operation = "+"
second_operand = 999
print(calculate(first_operand, operation, second_operand))

# 2 test

first_operand = 232
operation = "+"
second_operand = -100
print(calculate(first_operand, operation, second_operand))

# 3 test

first_operand = -100
operation = "-"
second_operand = 199
print(calculate(first_operand, operation, second_operand))

# 4 test

first_operand = 15678945621364865
operation = "+"
second_operand = 78545236468454135254549848946545215484878456465489998
print(calculate(first_operand, operation, second_operand))