# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list) -> dict:
    """
    Skapar en studentregister som kopplar namn till ålder.
    
    Parametrar:
    students (list): En lista med tuples där varje tuple innehåller (namn, ålder).
    
    Returvärde:
    dict: En dictionary där namnet är nyckeln och åldern är värdet.
    """
    student_register = {}
    for name, age in students:
        student_register[name] = age  # Lägg till namnet och åldern i dictionaryn
    return student_register

students_list = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
student_register = create_student_register(students_list)