# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

from typing import List

def sum_list(numbers: List[int]) -> int:
    """
    Returnerar summan av alla siffror i listan.
    
    Parametrar:
    numbers (List[int]): En lista med heltal.
    
    Returvärde:
    int: Summan av siffrorna i listan.
    """
    summan = 0
    for num in numbers:
        summan += num  # Summera varje nummer
    return summan

# Testa funktionen
#print(sum_list([-1, -2, -3]))  # Output: -6
print(sum_list([1, 2, 3]))      # Output: 6