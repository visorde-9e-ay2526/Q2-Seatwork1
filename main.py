#Com Arts List Checker
from pyscript import display, document


def view_user(e): #function
    document.getElementById('result').innerHTML = '' #Keeps the result blank when not used and deletes it when new result comes
    student_input = document.getElementById("fname").value #Gets the student's full name to be used as the student input
    comarts_members = ["Ma. Carizza N. Alfaro", "Cedric Philmund M. Visorde", "Georgina Erica A. Sarmiento", "Alexa Desiree C. Agnote"] #Valid student inputs
    student_checker = student_input in comarts_members #Checks if student input is valid/student is part of the club

    display_message = (f'Sorry {student_input}, you are not part of the Communication Arts Club.', f'Congratulations, {student_input}! You are part of the Communication Arts Club.') #Displays result
    display(display_message[student_checker], target='result') #Displays result
