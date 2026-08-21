class NotificationHandle:
    def __init__(self, observer):
        self.observer = observer
        self.observer_name = observer.__class__.__name__

    def update_observer(self, observer):
        observer.update()

