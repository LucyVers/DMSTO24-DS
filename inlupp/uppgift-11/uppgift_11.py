# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    """
    Räknar antalet ord i en given text.
    
    Parametrar:
    text (str): Texten som ska analyseras.
    
    Returvärde:
    int: Antalet ord i texten.
    """
    # Dela texten i ord, 'split()' delar strängen vid mellanslag
    words = text.split()
    return len(words)  # Returnera antalet ord

print(word_count("Detta är en enkel testtext."))