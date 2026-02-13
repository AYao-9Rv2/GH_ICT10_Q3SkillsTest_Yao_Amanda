from pyscript import display, document

def su(e):
    document.getElementById('output').innerHTML = ' '
    username = document.getElementById('username').value
    password = document.getElementById('password').value
 
    if len(username) < 7:
        display('username must contain at least 7 characters', target='output')

    elif len(password) < 10:
        display('password must be at least 10 characters long', target='output')

    elif not any(char.isalpha() for char in password):
        display('passowrd must contain at least one letter', target='output')

    elif not any(char.isdigit() for char in password):
        display('passowrd must contain at least one number', target='output')

    else:
        display('success! you now have a new account', target='output')