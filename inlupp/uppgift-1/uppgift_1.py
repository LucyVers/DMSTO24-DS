# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
    """
    Returnerar True om x är udda, annars False.
    
    Parametrar:
    x (int): Talet som ska kontrolleras.
    
    Returvärde:
    bool: True om x är udda, annars False.
    """
    return x % 2 == 1