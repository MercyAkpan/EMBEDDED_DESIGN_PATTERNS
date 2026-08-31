import random

class InverterProxy:
    def get_status(self):
        return {
            "voltage": round(random.uniform(220.0, 240.0), 1),
            "power": round(random.uniform(100.0, 500.0), 1),
            "battery": round(random.uniform(0.0, 100.0), 1)
        }


class RouterProxy:

    def get_status(self):
        return {
            "ip" : "192.345.647.12",
            "status" : "Low_power_mode",
            }
    
    def set_power_mode(self, mode):
        print(f"[ROUTER PROXY] Power mode changed to: {mode}")
