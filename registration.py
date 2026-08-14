while True:
    try:
        choise = int(input("Select an option: Log in - 1, Register - 2: "))
        
        if choise == 1:
            login = input("Enter your username: ")
            pasword = input("Enter your password: ")
            
            is_logged_in = False
            
            with open("registration.txt", "r") as file:
                for line in file:
                    saved_login, saved_pasword = line.strip().split(":")
                    if saved_login == login and saved_pasword == pasword:
                        print("Welcome!")
                        is_logged_in = True
                        break
            
            if is_logged_in:
                break
            else:
                print("Incorrect username or password. Please try again.")

        elif choise == 2:
            newlogin = input("Enter a new username: ")
            newpasword = input("Enter a new password: ")
            user_data = f"{newlogin}:{newpasword}\n"
            
            with open("registration.txt", "a") as file:
                file.write(user_data)
            
            print(f"Welcome {newlogin}! Your data has been saved.")
            break

        else:
            print("Invalid option selected. Please try again.")
            continue

    except ValueError:
        print("Error: Please enter a valid integer. Try again.")