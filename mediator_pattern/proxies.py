class InverterProxy:
    def get_status(self):
        return {
            "voltage": 230.0,
            "power": 450.0,
            "battery": 30.0
        }


class RouterProxy:

    def get_status(self):
        return {
            "ip" : "192.345.647.12",
            "status" : "Low_power_mode",
            }
    
    def set_power_mode(self, mode):
        print(f"[ROUTER PROXY] Power mode changed to: {mode}")
