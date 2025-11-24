import datetime

class Expense:
    
    def __init__(self, description, category, amount, date=None):
        self.description = description
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.date.today().isoformat()

    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data['description'], 
            data['category'], 
            data['amount'], 
            data['date']
        )
