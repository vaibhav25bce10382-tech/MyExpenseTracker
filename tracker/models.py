import datetime

class Expense:
    """
    Represents a single expense entry.
    Satisfies the 'Class/Object' technical expectation.
    """
    def __init__(self, description, category, amount, date=None):
        self.description = description
        self.category = category
        self.amount = amount
        # If no date is provided, use today's date
        self.date = date if date else datetime.date.today().isoformat()

    def to_dict(self):
        """Converts the object to a dictionary for saving to JSON."""
        return {
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        """Creates an Expense object from a dictionary."""
        return Expense(
            data['description'], 
            data['category'], 
            data['amount'], 
            data['date']
        )