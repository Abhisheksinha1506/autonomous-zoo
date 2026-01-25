def calculate_fibonacci_sequence(n_terms):
    
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    fibonacci_list = [0, 1]
    
    while len(fibonacci_list) < n_terms:
        
        last_number = fibonacci_list[-1]
        second_last_number = fibonacci_list[-2]
        next_number = last_number + second_last_number
        fibonacci_list.append(next_number)
        
    return fibonacci_list


if __name__ == "__main__":
    result = calculate_fibonacci_sequence(10)
    print(result)
