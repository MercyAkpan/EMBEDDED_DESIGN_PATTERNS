from mediator_pattern.proxies import InverterProxy, RouterProxy
from mediator_pattern.MediatorManager import EnergyManager
from time import sleep
from polling_pattern import poller
def main():
    inverter_proxy = InverterProxy()
    router_proxy = RouterProxy()
    energy_manager = EnergyManager(inverter_proxy, router_proxy)
    _poller = poller.Poller(inverter_proxy, router_proxy)

    running = True

    while running:
        status = _poller.poll()

        # status = inverter_proxy.get_status()

        log(status)

        # battery_level = status["battery"]

        energy_manager.handle_status(status)

        sleep(3)

def log(status):
    print(f"[MAIN] {status}")

if __name__ == "__main__":
    print(f"Running application")
    main()