def count_letters(string: str) -> dict:
    """
    Räknar förekomsten av varje bokstav i en given sträng.
    
    Parametrar:
    string (str): Strängen som ska analyseras.
    
    Returvärde:
    dict: En dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    letter_count = {}
    
    for char in string:
        if char.isalpha():  # Kontrollerar att tecknet är en bokstav
            char = char.lower()  # Gör bokstaven gemen för att räkna 'A' och 'a' som samma
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    return letter_count