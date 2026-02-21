def find_min(numbers):
    
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    
    min_val = numbers[0]
    
    for num in numbers:
        if num < min_val:
            min_val = num
            
    return min_val
