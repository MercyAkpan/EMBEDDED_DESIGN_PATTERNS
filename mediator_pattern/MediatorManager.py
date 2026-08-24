class EnergyManager:
    def __init__(self, inverterProxy, routerProxy):
        self.inverter_proxy = inverterProxy
        self.router_proxy = routerProxy

    def handle_inverter_battery_level(self, inverter_battery_level):
        if inverter_battery_level < 20:
            self.router_proxy.set_power_mode("saving")
        else:
            self.router_proxy.set_power_mode("normal")


    def handle_status(self, data):
        inverter_battery = data["inverter"]["battery"]
        self.handle_inverter_battery_level(inverter_battery)
        