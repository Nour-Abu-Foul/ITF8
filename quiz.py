#first quistion
while True:
    selections = int(input(f"""1. Palindrome
2. Even or Odd
Choose an option: """))

    if selections == 1:
        number = int(input("Enter the Number: "))
        num_str = str(number)
        reversed_str = num_str[::-1]

        if number == int(reversed_str):  # Convert reversed string back to integer
            print("The number is a Palindrome.")
        else:
            print("The number is not a Palindrome.")

    elif selections == 2:
        num = int(input("Enter the Number: "))
        if num % 2 == 0:
            print("The number is Even.")
        else:
            print("The Number is Odd.")

    else:
        print("Invalid Input")
    break

#second question
def find_smallest_largest_number():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    numbers.sort()
    largest_number = max(numbers)
    smallest_number = min(numbers)

    print("largert number: ",largest_number)
    print("smallest number: ",smallest_number)
find_smallest_largest_number()