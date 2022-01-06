from random import randint

print("Zain Eazad")
numbers = []
for _ in range(5):
    numbers.append(randint(0, 100))

print(numbers)
print(f"Average = {sum(numbers) / len(numbers)}")