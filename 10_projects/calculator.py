# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    print("=== Simple Calculator ===")
    
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"\n{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"\n{num1} ÷ {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Please enter valid numbers!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
