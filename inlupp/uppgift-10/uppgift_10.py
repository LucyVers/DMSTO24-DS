# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Konverterar en temperatur från Celsius till Fahrenheit.
    
    Parametrar:
    celsius (float): Temperaturen i grader Celsius.
    
    Returvärde:
    float: Temperaturen i grader Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit