class InverterProxy:
    def get_status(self):
        return {
            "voltage": 230.0,
            "power": 450.0,
            "battery": 13.0
        }


class RouterProxy:
    def set_power_mode(self, mode):
        print(f"[ROUTER PROXY] Power mode changed to: {mode}")
