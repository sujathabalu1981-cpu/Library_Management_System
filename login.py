# login.py

def login():
    username = "admin"
    password = "1234"

    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"


# calling the function
result = login()
print(result)
