# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
def validate_password(password: str) -> bool:
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    
    Parametrar:
    password (str): Lösenordet som ska valideras.
    
    Returvärde:
    bool: True om lösenordet är giltigt, annars False.
    """
    # Kontrollerar längden på lösenordet
    if len(password) < 8:
        return False
    
    # Kontrollerar om det finns minst en siffra i lösenordet
    if not any(char.isdigit() for char in password):
        return False
    
    return True 