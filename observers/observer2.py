class observer2:
    def __init__(self, subject):
        self.subject = subject
    
    def update(self):
        print("observer2 has been updated ")

    def install(self):
        self.subject.subscribe(self)

    def deinstall(self):
        self.subject.unsubscribe(self)

