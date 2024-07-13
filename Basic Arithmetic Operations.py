def main():
    print("You may do the following simple arithmetic operations:- \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
    
    while True:
        """ 
        Verifies that the input is either 1, 2, 3 or 4. 
        """ 
        user_input = input("Please choose 1, 2, 3 or 4. ")
        if user_input in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            
    """
    Gets the values of x and y from the user.
    """
    x, y = get_user_input()
    result = perform_operation(user_input, x, y)
    if result != None:
        print(f"Result of the operation is: {result}")
        

def get_user_input():
    x = validate_user_input("What's x? ")
    y = validate_user_input("What's y? ")
    return x, y


def perform_operation(user_input, x, y):
    try:  
        if user_input == "1":
            return x + y
        elif user_input == "2":
            return x - y
        elif user_input == "3":
            return x * y
        elif user_input == "4":
            return x / y
    except ZeroDivisionError:
        print("Error! Cannot divide by Zero.")
    
    
def validate_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numebr.")
  

if __name__ == "__main__":
    main()