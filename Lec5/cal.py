def calculate_stat(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) 
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum
numbers = [10, 20, 30, 40, 50]
total, avg, max_val, min_val = calculate_stat(numbers)
print(f"Total: {total}, Average: {avg}, Max: {max_val}, Min: {min_val}")