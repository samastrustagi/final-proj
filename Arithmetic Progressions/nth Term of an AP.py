def main():
    first_term = validate_int("Enter the first term of the AP: ")
    common_difference = validate_int("Enter the common difference of the AP: ")
    number_of_terms = validate_int("Enter the number of terms in the AP: ")
    
    nth_term = nth_term_of_ap(first_term, common_difference, number_of_terms)
    
    print(f"The {number_of_terms}th term of the AP is {nth_term}")
    
    
def nth_term_of_ap(a, d, n):
    return a + (n - 1) * d


def validate_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(f"Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
