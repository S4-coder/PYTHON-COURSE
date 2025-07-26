# Control Flow in Python with Real-World Examples

# 1. If-Else Statements
# Used in:
# - Age verification for websites
# - Payment processing
# - User access control
age = 18

if age >= 18:
    print("Access granted to adult content")    # Content restriction
elif age >= 13:
    print("Access granted to teen content")     # Teen-specific content
else:
    print("Access restricted - Kids only")      # Child protection

# 2. For Loops
# Used in:
# - Processing items in shopping cart
# - Sending bulk emails
# - Data analysis
print("\nProcessing orders:")
orders = ["Order#1", "Order#2", "Order#3", "Order#4", "Order#5"]
for order in orders:
    print(f"Processing {order}")

# 3. While Loops
# Used in:
# - Game loops
# - Download managers
# - Retry mechanisms
print("\nDownload progress example:")
progress = 0
while progress < 100:
    progress += 20
    print(f"Download progress: {progress}%")

# 4. Break and Continue
# Break used in:
# - Search operations
# - Input validation
# - Early exit conditions
print("\nSearch example:")
items = ["apple", "banana", "orange", "grape"]
search_for = "orange"
for item in items:
    if item == search_for:
        print(f"Found {search_for}!")
        break

# Continue used in:
# - Filtering data
# - Skipping unwanted items
# - Processing specific conditions
print("\nPayment processing example:")
transactions = [100, -50, 75, -25, 200]
for amount in transactions:
    if amount < 0:
        print(f"Skipping invalid amount: {amount}")
        continue
    print(f"Processing payment: ${amount}")

# 5. Match-Case (Python 3.10+)
# Used in:
# - Menu systems
# - Command processors
# - State machines
status_code = 404
match status_code:
    case 200:
        print("\nSuccess: Request completed")
    case 404:
        print("\nError: Page not found")
    case 500:
        print("\nError: Server error")
    case _:
        print("\nUnknown status code")
