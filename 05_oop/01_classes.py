# Object-Oriented Programming in Python with Real-World Applications

# Real-World Use Cases of OOP:
# 1. E-commerce Systems
# 2. Banking Applications
# 3. Game Development
# 4. Content Management Systems
# 5. Inventory Management

# Example: E-commerce System
class Product:
    # Class variable for store settings
    tax_rate = 0.1  # 10% tax
    
    def __init__(self, name, price, stock):
        # Instance variables - used in real product management
        self.name = name
        self.price = price
        self.stock = stock
        self.reviews = []  # Product reviews
    
    def get_total_price(self):
        """Calculate final price with tax - used in checkout"""
        return self.price + (self.price * self.tax_rate)
    
    def update_stock(self, quantity):
        """Update inventory - used in order processing"""
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False
    
    def add_review(self, rating, comment):
        """Add product review - used in review system"""
        self.reviews.append({"rating": rating, "comment": comment})
    
    @property
    def average_rating(self):
        """Get average product rating - used in product listing"""
        if not self.reviews:
            return 0
        return sum(review["rating"] for review in self.reviews) / len(self.reviews)

# Example: Shopping Cart (Inheritance)
class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price, float('inf'))  # Digital products have unlimited stock
        self.file_size = file_size
        self.download_link = None
    
    def generate_download_link(self):
        """Generate temporary download link - used in digital delivery"""
        import uuid
        self.download_link = f"https://example.com/download/{uuid.uuid4()}"
        return self.download_link

# Example: Order Management
class Order:
    order_counter = 0  # Track total orders
    
    def __init__(self, customer_name):
        Order.order_counter += 1
        self.order_id = f"ORD{Order.order_counter:04d}"
        self.customer_name = customer_name
        self.items = []
        self.status = "Pending"
    
    def add_item(self, product, quantity):
        """Add item to order - used in checkout process"""
        if product.update_stock(-quantity):
            self.items.append({"product": product, "quantity": quantity})
            return True
        return False
    
    def get_total(self):
        """Calculate order total - used in billing"""
        return sum(item["product"].get_total_price() * item["quantity"] 
                  for item in self.items)

# Real-World Usage Example
if __name__ == "__main__":
    # Creating products (like in an e-commerce system)
    laptop = Product("Gaming Laptop", 1299.99, 10)
    ebook = DigitalProduct("Python Guide", 29.99, "25MB")
    
    # Product reviews (like customer feedback system)
    laptop.add_review(5, "Excellent performance!")
    laptop.add_review(4, "Good but expensive")
    print(f"Laptop average rating: {laptop.average_rating}/5")
    
    # Processing an order (like checkout system)
    customer_order = Order("John Doe")
    customer_order.add_item(laptop, 1)
    customer_order.add_item(ebook, 1)
    
    # Order summary (like receipt generation)
    print(f"\nOrder ID: {customer_order.order_id}")
    print(f"Customer: {customer_order.customer_name}")
    print(f"Total Amount: ${customer_order.get_total():.2f}")
    
    # Digital product delivery
    if isinstance(ebook, DigitalProduct):
        download_link = ebook.generate_download_link()
        print(f"\nE-book download link: {download_link}")
    
    # Inventory check (like stock management system)
    print(f"\nLaptops in stock: {laptop.stock}")
    print(f"E-book file size: {ebook.file_size}")
