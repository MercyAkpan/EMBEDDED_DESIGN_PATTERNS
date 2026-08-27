class Logger:
    def __init__(self, subject=None):
        self.subject = subject
    
    def update(self, data):
        print("[LOGGER] Logger has been updated")
        self.log(data)

    def install(self):
        "it sends a pointer to itself"
        self.subject.subscribe(self)

    def deinstall(self):
        self.subject.unsubscribe(self)

    def log(self, data):
        print(f"[LOGGER] Logging...")
        print(f"[LOGGER] {data}")