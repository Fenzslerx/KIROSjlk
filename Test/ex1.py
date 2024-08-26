def find_single_occurrence_numbers(numbers: list) -> list:  
    seen_once = set()
    seen_more_than_once = set()

    for num in numbers:
        if num in seen_once:
            seen_once.discard(num)
            seen_more_than_once.add(num)
        elif num not in seen_more_than_once:
            seen_once.add(num)
        
    result = [num for num in numbers if num in seen_once]
    
    return result

# ตัวอย่างการใช้งาน:
print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))  # Output: [6, 7, 8]
print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4]))  # Output: [1]
print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6]))     # Output: [1, 2, 3, 4, 5, 6]
print(find_single_occurrence_numbers([1, 1, 1, 1, 1]))        # Output: []

