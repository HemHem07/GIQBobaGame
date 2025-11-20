class Employee:
    def __init__(self, name, wage, capacity):
        self.name = name
        self.wage = wage
        self.capacity = capacity 
    def __str__(self):
        return f"Name: {self.name}, Daily Wage: {self.wage}, Customer Capacity Per Turn: {self.capacity}"
