from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type, timestamp=datetime.now()):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: {self.amount}"