class observer1:
    def __init__(self, subject):
        self.subject = subject
    
    def update(self):
        print("observer1 has been updated")

    def install(self):
        "it sends a pointer to itsself"
        self.subject.subscribe(self)

    def deinstall(self):
        self.subject.unsubscribe(self)

