# Advanced Python Topics with Real-World Applications

# Real-World Use Cases:
# 1. Performance Monitoring
# 2. Data Processing
# 3. Resource Management
# 4. API Development
# 5. Parallel Computing

# 1. Decorators - Used in:
# - Authentication
# - Logging
# - Caching
# - API Rate Limiting
def log_function_call(func):
    """Logger Decorator - Used in application monitoring"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned: {result}")
        return result
    return wrapper

def cache_result(func):
    """Caching Decorator - Used in performance optimization"""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"[CACHE] Returning cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Example: API Rate Limiting
class RateLimiter:
    """Rate Limiting Decorator - Used in API services"""
    def __init__(self, max_calls=100, time_window=3600):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            # Remove old calls
            self.calls = [call_time for call_time in self.calls 
                         if current_time - call_time <= self.time_window]
            
            if len(self.calls) >= self.max_calls:
                raise Exception("Rate limit exceeded")
            
            self.calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper

# 2. Generators - Used in:
# - Large Data Processing
# - Memory Efficient Operations
# - Streaming Data
class DataProcessor:
    """Example: Large File Processing"""
    @staticmethod
    def process_large_file(filename):
        def line_processor():
            with open(filename, 'r') as file:
                for line in file:
                    # Process line by line without loading entire file
                    yield line.strip().upper()
        
        return line_processor()

# 3. Context Managers - Used in:
# - Resource Management
# - Database Connections
# - File Operations
class DatabaseConnection:
    """Example: Database Session Management"""
    def __init__(self, connection_string):
        self.conn_string = connection_string
    
    def __enter__(self):
        print(f"Connecting to database: {self.conn_string}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        return True

# 4. Property Decorators - Used in:
# - Data Validation
# - Computed Properties
# - Encapsulation
class Product:
    """Example: E-commerce Product"""
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._discount = 0
    
    @property
    def price(self):
        """Get final price after discount"""
        return self._price * (1 - self._discount)
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not 0 <= value <= 1:
            raise ValueError("Discount must be between 0 and 1")
        self._discount = value

# 5. Magic Methods - Used in:
# - Custom Data Structures
# - Operator Overloading
# - Object Representation
class ShoppingCart:
    """Example: Shopping Cart Implementation"""
    def __init__(self):
        self.items = {}
    
    def __setitem__(self, product_name, quantity):
        self.items[product_name] = quantity
    
    def __getitem__(self, product_name):
        return self.items.get(product_name, 0)
    
    def __str__(self):
        return f"Cart with {len(self.items)} items"
    
    def __len__(self):
        return sum(self.items.values())

# 6. Multiprocessing - Used in:
# - Data Analysis
# - Image Processing
# - Batch Operations
from multiprocessing import Pool
import os
import time

class ImageProcessor:
    """Example: Parallel Image Processing"""
    @staticmethod
    def process_image(image_path):
        # Simulate image processing
        time.sleep(0.1)
        return f"Processed {image_path}"
    
    @staticmethod
    def batch_process(image_paths):
        with Pool(processes=os.cpu_count()) as pool:
            results = pool.map(ImageProcessor.process_image, image_paths)
        return results

# Real-World Usage Examples
if __name__ == "__main__":
    # 1. Decorator Example - API Rate Limiting
    @RateLimiter(max_calls=2, time_window=5)
    def api_request():
        return "API Response"
    
    print("Testing API Rate Limiting:")
    try:
        for _ in range(3):
            print(api_request())
    except Exception as e:
        print(f"Rate limit error: {e}")
    
    # 2. Generator Example - Processing Large Data
    print("\nProcessing Large File (Simulation):")
    processor = DataProcessor()
    for line in processor.process_large_file("sample.txt"):
        print(f"Processed: {line[:30]}...")
    
    # 3. Context Manager Example - Database
    print("\nDatabase Operations:")
    with DatabaseConnection("mysql://localhost/db") as db:
        print("Performing database operations...")
    
    # 4. Property Example - E-commerce
    print("\nProduct Management:")
    product = Product("Laptop", 1000)
    product.discount = 0.1
    print(f"Product price after 10% discount: ${product.price}")
    
    # 5. Magic Methods Example - Shopping Cart
    print("\nShopping Cart Operations:")
    cart = ShoppingCart()
    cart["laptop"] = 1
    cart["mouse"] = 2
    print(cart)
    print(f"Total items in cart: {len(cart)}")
    
    # 6. Multiprocessing Example - Batch Processing
    print("\nParallel Processing:")
    images = [f"image_{i}.jpg" for i in range(5)]
    results = ImageProcessor.batch_process(images)
    for result in results:
        print(result)
