def main():
    x, y = get_user_input()
    try:    
        print(x / y)
    except ZeroDivisionError:
        print("Invalid input. Can't divide by zero.")


def get_user_input():
    x = validate_user_input("What's x? ")
    y = validate_user_input("What's y? ")
    return x, y
    
def validate_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numebr.")
            
    
if __name__ == "__main__":
    main()