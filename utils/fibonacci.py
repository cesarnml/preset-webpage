def fibonacci_recursive(n):
    """
    Generate the nth Fibonacci number using recursion.
    
    The Fibonacci sequence is defined as:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_sequence(length):
    """
    Generate a Fibonacci sequence up to the specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list containing the Fibonacci sequence
        
    Raises:
        ValueError: If length is negative
        TypeError: If length is not an integer
    """
    # Input validation
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    if length < 0:
        raise ValueError("Length must be non-negative")
    
    return [fibonacci_recursive(i) for i in range(length)]


# Example usage
if __name__ == "__main__":
    # Generate first 10 numbers in the Fibonacci sequence
    fib_sequence = generate_fibonacci_sequence(10)
    print(f"First 10 Fibonacci numbers: {fib_sequence}")
    
    # Calculate the 20th Fibonacci number
    fib_20 = fibonacci_recursive(20)
    print(f"The 20th Fibonacci number is: {fib_20}")