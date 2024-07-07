def get_num(prompt):
    num = input(prompt)
    return float(num)

def multiply(num1, num2):
    return float(num1) * float(num2)

num1 = get_num("Enter the first number: ")
num2 = get_num("Enter the second number: ")
product = multiply(num1, num2)

print(f'{num1} * {num2} = {product}')