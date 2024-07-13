def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

def main():
    while True:
           
        try:
            n = int(input("Please enter a non-negative integer to find out its Factorial: "))
            if n < 0:
                print("Error! Factorial is not defined for a negative number.")
            else:
                result = factorial(n)
                print(f"The factorial of {n} is {result}")
                break
            
        except ValueError:
            print(f"Invalid input. Please enter a non-negative integer.")
            
            
if __name__ == "__main__":
    main()
    
    
    
    
    
# iterative call can be used as well. (keeping in mind big o notation and runtime)
