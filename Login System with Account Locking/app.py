

# Predefined user credentials
users = {"john":"password123", "elliot":"mrrobot"}

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password")

    if username in users and users[username] == password:
        print("Login sucessfull! Welcome,", username)
        break
    else:
        attempts += 1
        print(f"Incorrect credentials! Attempt left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("Account locked due to multiple failed attempts")



