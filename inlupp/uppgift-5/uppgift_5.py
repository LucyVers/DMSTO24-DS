def filter_odd(numbers: list) -> list:
    """
    Filtrerar ut udda tal från en lista.
    
    Parametrar:
    numbers (list): En lista med heltal.
    
    Returvärde:
    list: En lista som innehåller endast de jämna talen.
    """
    return [num for num in numbers if num % 2 == 0]
