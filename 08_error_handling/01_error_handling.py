# Error Handling in Python with Real-World Applications

# Real-World Use Cases:
# 1. Form Validation
# 2. File Operations
# 3. API Interactions
# 4. Database Operations
# 5. User Input Validation

class InvalidPasswordError(Exception):
    """Custom exception for password validation - Used in authentication systems"""
    pass

class InsufficientFundsError(Exception):
    """Custom exception for banking operations - Used in financial systems"""
    pass

class PaymentProcessor:
    """Example: Payment Processing System"""
    def __init__(self):
        self.balance = 1000  # Sample account balance
    
    def process_payment(self, amount):
        """Process payment - Used in e-commerce systems"""
        try:
            if amount <= 0:
                raise ValueError("Payment amount must be positive")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds in account")
            
            self.balance -= amount
            return {"status": "success", "remaining_balance": self.balance}
            
        except InsufficientFundsError as e:
            return {"status": "error", "message": str(e)}
        except ValueError as e:
            return {"status": "error", "message": str(e)}
        except Exception as e:
            return {"status": "error", "message": "Payment processing failed"}

class UserAuthenticator:
    """Example: User Authentication System"""
    def validate_password(self, password):
        """Password validation - Used in registration systems"""
        try:
            if len(password) < 8:
                raise InvalidPasswordError("Password must be at least 8 characters")
            if not any(c.isupper() for c in password):
                raise InvalidPasswordError("Password must contain at least one uppercase letter")
            if not any(c.isdigit() for c in password):
                raise InvalidPasswordError("Password must contain at least one number")
            return True
        except InvalidPasswordError as e:
            print(f"Password Error: {e}")
            return False

class DatabaseConnection:
    """Example: Database Connection Handler"""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        """Context manager for database connection - Used in data access layers"""
        try:
            print(f"Connecting to database: {self.connection_string}")
            # Simulate database connection
            self.connection = True
            return self
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Safe database disconnection"""
        if self.connection:
            print("Closing database connection")
            self.connection = None
        return False

class FileProcessor:
    """Example: File Processing System"""
    @staticmethod
    def process_data_file(filename):
        """Process data file - Used in data processing systems"""
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
                return {"status": "success", "lines": len(data)}
        except FileNotFoundError:
            return {"status": "error", "message": f"File {filename} not found"}
        except PermissionError:
            return {"status": "error", "message": "Permission denied to access file"}
        except Exception as e:
            return {"status": "error", "message": f"Error processing file: {str(e)}"}
        finally:
            print("File processing attempt completed")

# Real-World Usage Examples
if __name__ == "__main__":
    # 1. Payment Processing Example
    print("Payment Processing Example:")
    payment = PaymentProcessor()
    result = payment.process_payment(500)
    print(f"Payment Result: {result}")
    
    result = payment.process_payment(1000)  # Try to pay more than balance
    print(f"Payment Result: {result}")
    
    # 2. Password Validation Example
    print("\nPassword Validation Example:")
    auth = UserAuthenticator()
    print("Validating password 'password123':", auth.validate_password("password123"))
    print("Validating password 'Password123':", auth.validate_password("Password123"))
    
    # 3. Database Connection Example
    print("\nDatabase Connection Example:")
    try:
        with DatabaseConnection("mysql://localhost:3306/mydb") as db:
            print("Performing database operations...")
            # Simulate database operations
    except Exception as e:
        print(f"Database operation failed: {e}")
    
    # 4. File Processing Example
    print("\nFile Processing Example:")
    result = FileProcessor.process_data_file("nonexistent.txt")
    print(f"File processing result: {result}")
    
    # 5. Custom Error Handling in Banking
    try:
        balance = 100
        withdrawal = 150
        if withdrawal > balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${withdrawal}. Balance is ${balance}"
            )
    except InsufficientFundsError as e:
        print(f"\nBanking Error: {e}")
