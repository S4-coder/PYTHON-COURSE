# Working with Modules and Packages - Real-World Applications

# 1. Math Module - Real Uses:
# - Financial Calculations
# - Scientific Computing
# - Game Physics
import math

def calculate_loan_payment(principal, rate, years):
    """Calculate monthly loan payment - Used in banking apps"""
    monthly_rate = rate / 12 / 100
    months = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(payment, 2)

# Example: Mortgage Calculator
loan_amount = 200000
annual_rate = 4.5
loan_years = 30
monthly_payment = calculate_loan_payment(loan_amount, annual_rate, loan_years)
print(f"Monthly Mortgage Payment: ${monthly_payment}")

# 2. Random Module - Real Uses:
# - Game Development
# - Data Sampling
# - Security (Token Generation)
import random
import string

def generate_password(length=12):
    """Generate secure password - Used in authentication systems"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Example: Security Token Generator
print(f"\nGenerated Password: {generate_password()}")

# 3. DateTime Module - Real Uses:
# - Scheduling Systems
# - Event Management
# - Log Systems
import datetime

def calculate_age(birthdate):
    """Calculate age - Used in healthcare/insurance systems"""
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Example: Appointment Scheduler
class Appointment:
    def __init__(self, title, datetime_obj):
        self.title = title
        self.datetime = datetime_obj
        
    def get_reminder_time(self):
        """Get reminder time (15 minutes before) - Used in calendar apps"""
        return self.datetime - datetime.timedelta(minutes=15)

# Create appointment
appt_time = datetime.datetime.now() + datetime.timedelta(days=1)
appointment = Appointment("Doctor Visit", appt_time)
print(f"\nAppointment: {appointment.title}")
print(f"Time: {appointment.datetime.strftime('%Y-%m-%d %H:%M')}")
print(f"Reminder Time: {appointment.get_reminder_time().strftime('%Y-%m-%d %H:%M')}")

# 4. JSON Module - Real Uses:
# - API Integration
# - Configuration Management
# - Data Storage
import json

class UserProfile:
    def __init__(self, name, email, preferences):
        self.name = name
        self.email = email
        self.preferences = preferences
    
    def save_to_json(self, filename):
        """Save user profile - Used in app settings"""
        data = {
            "name": self.name,
            "email": self.email,
            "preferences": self.preferences
        }
        return json.dumps(data, indent=4)
    
    @classmethod
    def load_from_json(cls, json_string):
        """Load user profile - Used in app initialization"""
        data = json.loads(json_string)
        return cls(data["name"], data["email"], data["preferences"])

# Example: User Settings Management
user = UserProfile(
    "John Doe",
    "john@example.com",
    {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    }
)

# Save user settings
json_data = user.save_to_json("profile.json")
print("\nSaved User Profile:")
print(json_data)

# Load user settings
loaded_user = UserProfile.load_from_json(json_data)
print("\nLoaded User Preferences:", loaded_user.preferences)
