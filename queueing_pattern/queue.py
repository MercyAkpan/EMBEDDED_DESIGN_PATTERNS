class MessageQueue:
    def __init__(self):
        self.message = None

    def insert(self, message):
        if self.message is None:
            self.message = message
            return True
        return False

    def remove(self):
        message = self.message
        self.message = None
        return message