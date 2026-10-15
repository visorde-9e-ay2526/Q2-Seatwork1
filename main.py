#Com Arts List Checker
from pyscript import display, document


def view_user(e): #function
    document.getElementById('result').innerHTML = ''
    student_input = document.getElementById("fname").value
    comarts_members = ["Ma. Carizza N. Alfaro", "Cedric Philmund M. Visorde", "Georgina Erica A. Sarmiento", "Alexa Desiree C. Agnote"]
    student_checker = student_input in comarts_members

    display_message = (f'Sorry {student_input}, you are not part of the Communication Arts Club.', f'Congratulations, {student_input}! You are part of the Communication Arts Club.')
    display(display_message[student_checker], target='result')
