password = "abc123"

for i in range (3, 0, -1):
    attempt = input("Enter password: ")
    if attempt == password:
        break
    else:
        print("Incorrect - try again!")

if i == 1:
    print("You have been denied access")
else:
    print("Password has been accepted.")
