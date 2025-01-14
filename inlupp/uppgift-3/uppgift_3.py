# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list[int]) -> int:
    """
    Returnerar det största talet i en lista.
    
    Parametrar:
    numbers (list[int]): En lista med heltal.
    
    Returvärde:
    int: Det största talet i listan.
    """
    return max(numbers)  # Använder den inbyggda max-funktionen för att hitta det största talet

# Testa funktionen
print(max_in_list([1, 2, 3]))