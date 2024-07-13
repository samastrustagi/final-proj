def main():
    first_term = validate_int("Enter the first term of the AP: ")
    common_difference = validate_int("Enter the common difference of the AP: ")
    number_of_terms = validate_int("Enter the number of terms in the AP: ")
    
    sum_of_nth_term = sum_nth_term(first_term, common_difference, number_of_terms)
    
    print(f"The sum of first {number_of_terms} terms of the AP is {sum_of_nth_term}")
    
    
def sum_nth_term(a, d, n):
    return n / 2 * (2 * a + (n - 1) * d)


def validate_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(f"Invalid input! Please enter an integer.")
    

if __name__ == "__main__":
    main()
