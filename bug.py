def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (potential error)
averages = []
for i in range(5):
    random_numbers = [random.randint(1, 100) for _ in range(random.randint(1, 10))] 
    averages.append(calculate_average(random_numbers))
print(averages)