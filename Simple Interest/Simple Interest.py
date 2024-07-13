def main():
    principal_amount, interest_rate, time = get_input()
    print(f"The interest is {principal_amount * interest_rate * time / 100}")
    
    
def get_input():
    principal_amount = validate_user_input("Please enter the Principal Amount (in Dollars): ")
    interest_rate = validate_user_input("Please enter the Rate of Interest (per annum): ")
    time = validate_user_input("Please enter the time period (per annum): ")
    return principal_amount, interest_rate, time


def validate_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            

if __name__ == "__main__":
    main()
