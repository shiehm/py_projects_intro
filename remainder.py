def remainders_3(numbers):
    return [number % 3 for number in numbers]

# This one tests to see if any numbers are NOT divisible by 3
def contains_1(numbers):
    return any(remainders_3(numbers))

# This one tests to see if any numbers are ARE divisible by 3
def contains_0(numbers):
    remainders = remainders_3(numbers)
    test = [True for remainder in remainders if remainder == 0]
    return any(test)
    
# This one tests to see if all numbers are NOT divisible by 3
def none_0(numbers):
    return all(remainders_3(numbers))

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(contains_1(numbers_1))
print(contains_1(numbers_2))
print(contains_1(numbers_3))
print(contains_1(numbers_4))

print()

print(contains_0(numbers_1))
print(contains_0(numbers_2))
print(contains_0(numbers_3))
print(contains_0(numbers_4))

print()

print(none_0(numbers_1))
print(none_0(numbers_2))
print(none_0(numbers_3))
print(none_0(numbers_4))