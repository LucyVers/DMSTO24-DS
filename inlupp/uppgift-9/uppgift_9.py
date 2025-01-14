# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string: str) -> bool:
    """
    Kontrollerar om en given sträng är ett palindrom.
    
    Parametrar:
    string (str): Strängen som ska kontrolleras.
    
    Returvärde:
    bool: True om strängen är ett palindrom, annars False.
    """
    # Rengör strängen genom att ta bort mellanslag och göra den gemen
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Jämför den rengjorda strängen med sin omvända version
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("Hello"))



