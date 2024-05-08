
numbers = list(range(1, 11))

squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

last_numb = squared_numbers.pop()
print(last_numb)