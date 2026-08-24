class Poller:

    def __init__(self, inverter, router):
        self.inverter = inverter
        self.router = router

    def poll(self):
        inverter_data = self.inverter.get_status()
        router_data = self.router.get_status()

        return {
            "inverter": inverter_data,
            "router": router_data
        }