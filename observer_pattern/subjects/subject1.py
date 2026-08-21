from subjects import Notificationhandle

class subject1:
    def __init__(self):
        self.listofNotificationHandle = []

    def subscribe(self, observer):
        print(f"[SUBJECT] Subscribing...")
        handle = Notificationhandle.NotificationHandle(observer)
        self.listofNotificationHandle.append(handle)
        print(f"[SUBJECT] Observer {handle.observer_name} has been added")

    def unsubscribe(self, observer):
        print(f"[SUBJECT] Length of Handle list: {len(self.listofNotificationHandle)} ")
        target_index = next(
        (i for i, obj in enumerate(self.listofNotificationHandle) if obj.observer == observer), None)

        if target_index is not None:
            target_object = self.listofNotificationHandle[target_index]        

            del self.listofNotificationHandle[target_index]

        print(f"[SUBJECT] Length of Handle list: {len(self.listofNotificationHandle)} ")

    def insert(self, data):
        print(f"Data added: {data}")
        self.notify()

    def notify(self):
        print(f"[SUBJECT] Notifying Subscribers")
        for handle in self.listofNotificationHandle:
            print(f"Notifiying {handle.observer_name} ")
            handle.update_observer(handle.observer)
