class EnergyManager:
    def __init__(self, inverterProxy, routerProxy):
        self.inverter_proxy = inverterProxy
        self.router_proxy = routerProxy

    def handle_battery_level(self, inverter_battery_level):
        if inverter_battery_level < 20:
            self.router_proxy.set_power_mode("saving")
        else:
            self.router_proxy.set_power_mode("normal")

    