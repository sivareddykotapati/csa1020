def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Invalid Username or Password"


# Sample test
user = input("Enter username: ")
pwd = input("Enter password: ")
print(login(user, pwd))
