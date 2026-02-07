# login.py
# Simple login module (no user input)
<<<<<<< HEAD
print("Login Module from MASTER branch")
======
print("Login Module from Master branch")
>>>>>>> conflict-branch
def login():
    username = "admin"
    password = "admin123"

    if username == "admin" and password == "admin123":
        return "Login successful"
    else:
        return "Login failed"


# Calling the function
result = login()
print(result)
