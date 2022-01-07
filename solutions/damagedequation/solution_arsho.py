"""
Title     : Damaged Equation
Source    : IDI Open 2021
URL       : https://open.kattis.com/problems/damagedequation
Author    : arsho
Created   : 06 January 2022
"""


def get_result(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return None
        return a // b


def get_valid_equation(ar, op1, op2):
    left_side = get_result(ar[0], ar[1], op1)
    right_side = get_result(ar[2], ar[3], op2)
    if left_side == None or right_side == None:
        return False
    if left_side == right_side:
        return f"{ar[0]} {op1} {ar[1]} = {ar[2]} {op2} {ar[3]}"
    return False


ar = list(map(int, input().split()))
valid_equations = []
operators = ["+", "-", "*", "/"]
for op1 in operators:
    for op2 in operators:
        eq = get_valid_equation(ar, op1, op2)
        if eq:
            valid_equations.append(eq)

valid_equations = sorted(valid_equations)
if len(valid_equations) == 0:
    print("problems ahead")
else:
    for equation in valid_equations:
        print(equation)
