# Functions in Python with Real-World Applications

# 1. Basic Function
# Used in:
# - User greeting in applications
# - API response formatting
# - Data transformation
def greet(name):
    """This function greets the person passed in as parameter"""
    return f"Hello, {name}!"

# 2. Function with Multiple Parameters
# Used in:
# - Calculator applications
# - Financial calculations
# - Data analysis
def calculate_total(price, quantity, discount=0):
    """Calculate total price with discount"""
    subtotal = price * quantity
    return subtotal - (subtotal * discount)

# 3. Function with Default Parameters
# Used in:
# - Configuration settings
# - API requests
# - Image processing
def format_text(text, font_size=12, color="black", bold=False):
    """Format text with default styling options"""
    style = f"Size: {font_size}, Color: {color}"
    if bold:
        style += ", Weight: Bold"
    return f"Text: '{text}' with {style}"

# 4. Function with *args
# Used in:
# - Log systems
# - Event handling
# - Data aggregation
def log_events(*events):
    """Log multiple events with timestamps"""
    from datetime import datetime
    for event in events:
        print(f"[{datetime.now()}] {event}")

# 5. Function with **kwargs
# Used in:
# - User profile updates
# - Database record updates
# - Configuration management
def update_user_profile(**user_data):
    """Update user profile with any number of fields"""
    profile = {}
    for field, value in user_data.items():
        profile[field] = value
        print(f"Updated {field} to: {value}")
    return profile

# 6. Lambda Functions
# Used in:
# - Data filtering
# - Sorting custom objects
# - Quick calculations
sort_by_price = lambda product: product['price']
filter_active = lambda user: user['status'] == 'active'

# Main program with real-world examples
if __name__ == "__main__":
    # 1. Greeting System
    print(greet("New User"))  # Welcome message in app
    
    # 2. E-commerce Calculations
    print(f"Order total: ${calculate_total(price=29.99, quantity=2, discount=0.1)}")
    
    # 3. Text Formatting System
    print(format_text("Warning!", font_size=16, color="red", bold=True))
    
    # 4. Logging System
    log_events(
        "User logged in",
        "Profile updated",
        "Order placed #12345"
    )
    
    # 5. User Profile System
    update_user_profile(
        username="john_doe",
        email="john@example.com",
        age=25,
        location="New York"
    )
    
    # 6. Data Processing with Lambda
    products = [
        {'name': 'Laptop', 'price': 999},
        {'name': 'Mouse', 'price': 29.99},
        {'name': 'Keyboard', 'price': 59.99}
    ]
    # Sort products by price
    sorted_products = sorted(products, key=sort_by_price)
    print("\nProducts sorted by price:", sorted_products)
