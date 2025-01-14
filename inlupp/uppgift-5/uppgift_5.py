def filter_odd(numbers: list) -> list:
    """
    Filtrerar ut udda tal från en lista.
    
    Parametrar:
    numbers (list): En lista med heltal.
    
    Returvärde:
    list: En lista som innehåller endast de udda talen.
    """
    return [num for num in numbers if num % 2 != 0]

print(filter_odd([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]