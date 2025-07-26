# Python Data Types and Their Real-World Applications

# 1. Numbers in Real-World:
integer_num = 42          # Used in: Counting items, Age, Quantity
float_num = 3.14         # Used in: Prices, Scientific calculations, Measurements
complex_num = 2 + 3j     # Used in: Signal processing, Electrical engineering

print("Integer:", integer_num)  # Example: Number of products in cart
print("Float:", float_num)      # Example: Product price
print("Complex:", complex_num)   # Example: Signal analysis

# 2. Strings in Real Applications:
# Used in: User names, Addresses, Text processing
text = "Hello Python"
multiline_text = '''Dear Customer,
Thank you for your order.
Your order #12345 has been confirmed.'''  # Email template example

print("\nString:", text)
print("Length of string:", len(text))      # Checking password length
print("Multiline string:", multiline_text)

# 3. Lists in Practice:
# Used in: Todo lists, Shopping carts, Playlists
my_list = [1, 2, 3, "Python", True]        # Mixed data shopping cart
print("\nList:", my_list)
print("First element:", my_list[0])
my_list.append("New Item")                  # Adding item to cart
print("After append:", my_list)

# 4. Tuples in Applications:
# Used in: Geographic coordinates, RGB colors, Fixed data
my_tuple = (1, 2, 3, "Python")             # Coordinates example
print("\nTuple:", my_tuple)

# 5. Dictionaries in Real Use:
# Used in: User profiles, Configuration settings, Data mapping
my_dict = {
    "name": "Python",                       # User profile example
    "version": 3.9,
    "is_active": True
}
print("\nDictionary:", my_dict)
print("Accessing value:", my_dict["name"])  # Getting user info

# 6. Sets in Practice:
# Used in: Removing duplicates, Unique values, Group memberships
my_set = {1, 2, 3, 3, 4, 4, 5}  # Unique user IDs
print("\nSet:", my_set)
