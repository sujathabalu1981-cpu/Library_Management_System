# login.py

def login():
    username = "admin"
    password = "1234"

    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

print(login())
