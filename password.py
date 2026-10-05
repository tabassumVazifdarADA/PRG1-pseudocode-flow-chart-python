attempts = 0

while attempts < 3:
    password = input("Enter your password: ")

    if password == "password123":
        print("You are logged in successfully.")
        break
    else:
        attempts += 1
        print("Incorrect password.")

if attempts == 3:
    print("Your account is locked. No further attempts are allowed.")