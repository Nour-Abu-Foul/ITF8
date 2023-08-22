with open('new_file.txt', "a") as file:

    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    user_info = f"""User Name: {user_name}" 
    Age: {user_age}" 
    Date of Birth: {date_of_birth}"""
    file.write(user_info)
