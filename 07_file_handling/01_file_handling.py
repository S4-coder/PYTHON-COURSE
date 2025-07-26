# File Handling in Python with Real-World Applications

# Real-World Use Cases:
# 1. Log Systems
# 2. Data Analysis
# 3. Configuration Management
# 4. User Data Storage
# 5. Report Generation

import csv
import json
from datetime import datetime

class LogSystem:
    """Example: Application Logging System"""
    def __init__(self, log_file):
        self.log_file = log_file
    
    def log_event(self, event_type, message):
        """Log events - Used in error tracking and monitoring"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event_type}: {message}\n"
        
        with open(self.log_file, "a") as file:
            file.write(log_entry)

class UserDataManager:
    """Example: User Profile Management System"""
    def __init__(self, data_file):
        self.data_file = data_file
    
    def save_user(self, user_data):
        """Save user profile - Used in registration systems"""
        try:
            with open(self.data_file, "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=user_data.keys())
                if file.tell() == 0:  # File is empty
                    writer.writeheader()
                writer.writerow(user_data)
            return True
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False
    
    def get_all_users(self):
        """Retrieve all users - Used in admin panels"""
        users = []
        try:
            with open(self.data_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    users.append(row)
            return users
        except FileNotFoundError:
            return []

class ConfigManager:
    """Example: Application Configuration Management"""
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration - Used in app initialization"""
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def save_config(self):
        """Save configuration - Used in settings management"""
        with open(self.config_file, "w") as file:
            json.dump(self.config, file, indent=4)
    
    def update_setting(self, key, value):
        """Update configuration - Used in settings updates"""
        self.config[key] = value
        self.save_config()

class ReportGenerator:
    """Example: Business Report Generation"""
    def __init__(self, data_file, report_file):
        self.data_file = data_file
        self.report_file = report_file
    
    def generate_sales_report(self):
        """Generate sales report - Used in business analytics"""
        try:
            # Read sales data
            with open(self.data_file, "r") as file:
                reader = csv.DictReader(file)
                sales_data = list(reader)
            
            # Calculate totals
            total_sales = sum(float(row['amount']) for row in sales_data)
            
            # Generate report
            report = f"""Sales Report - {datetime.now().strftime('%Y-%m-%d')}
Total Sales: ${total_sales:,.2f}
Number of Transactions: {len(sales_data)}
"""
            # Save report
            with open(self.report_file, "w") as file:
                file.write(report)
            
            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False

# Real-World Usage Examples
if __name__ == "__main__":
    # 1. Application Logging
    logger = LogSystem("app.log")
    logger.log_event("INFO", "Application started")
    logger.log_event("ERROR", "Database connection failed")
    
    # 2. User Management
    user_manager = UserDataManager("users.csv")
    user_manager.save_user({
        "username": "john_doe",
        "email": "john@example.com",
        "joined_date": datetime.now().strftime("%Y-%m-%d")
    })
    
    # 3. Configuration Management
    config = ConfigManager("config.json")
    config.update_setting("theme", "dark")
    config.update_setting("language", "en")
    
    # 4. Report Generation
    reporter = ReportGenerator("sales.csv", "sales_report.txt")
    if reporter.generate_sales_report():
        print("Sales report generated successfully")
    
    # Print stored users
    print("\nRegistered Users:")
    for user in user_manager.get_all_users():
        print(f"Username: {user['username']}, Email: {user['email']}")
