def fizzbuzz(n :int)  ->list[str]:
    """
    Generate the fizzbuzz sequence from 1 to n.
    
    Args:
        n (int): The upper limit of the sequence (inclusive).
        
    Returns:
        list[str]: The fizzbuzz sequence as a list of strings.
         Time Complexity:
        O(n), because each number from 1 to n is processed once.

    Space Complexity:
        O(n), because the result list stores n values.
    
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result