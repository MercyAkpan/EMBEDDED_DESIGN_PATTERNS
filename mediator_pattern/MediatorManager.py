from single_event_receptor_pattern.event import EventType, Event 


class EnergyManager:
    def __init__(self, inverterProxy, routerProxy, state_machine):
        self.inverter_proxy = inverterProxy
        self.router_proxy = routerProxy
        self.state_machine = state_machine
    
    def handle_inverter_battery_level(self, inverter_battery_level):
        if inverter_battery_level < 20:
            event = Event(EventType.BATTERY_CRITICAL)

            self.state_machine.event_dispatch(event)

            self.router_proxy.set_power_mode("saving")

        elif inverter_battery_level < 50:
            event = Event(EventType.BATTERY_LOW)

            self.state_machine.event_dispatch(event)

            self.router_proxy.set_power_mode("saving")
        else:
            event = Event(EventType.BATTERY_NORMAL)

            self.state_machine.event_dispatch(event)

            self.router_proxy.set_power_mode("normal")


    def handle_status(self, data):
        inverter_battery = data["inverter"]["battery"]
        self.handle_inverter_battery_level(inverter_battery)

    def update(self, data):
        print("[MEDIATOR] Mediator has been updated")
        self.handle_status(data)

    def install(self):
        "it sends a pointer to itsself"
        self.subject.subscribe(self)

    def deinstall(self):
        self.subject.unsubscribe(self)