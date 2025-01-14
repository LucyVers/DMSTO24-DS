# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.
def multiplication_table(n: int, limit: int) -> list:
    """
    Skapar multiplikationstabellen för n upp till limit.
    
    Parametrar:
    n (int): Talet för vilket multiplikationstabellen ska skapas.
    limit (int): Det högsta värdet i multiplikationstabellen.
    
    Returvärde:
    list: En lista som innehåller multiplikationstabellen för n.
    """
    return [n * i for i in range(1, limit + 1)]
print(multiplication_table(3, 5))    # Output: [3, 6, 9, 12, 15]