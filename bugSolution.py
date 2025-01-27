import random
def calculate_average(numbers):
    try:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0  # Handle the case where len(numbers) is 0 after the initial check
    except TypeError:
        return 0 # handle invalid data types

averages = []
for i in range(5):
    random_numbers = [random.randint(1, 100) for _ in range(random.randint(0, 10))]  # Allow for empty lists
    averages.append(calculate_average(random_numbers))
print(averages) 