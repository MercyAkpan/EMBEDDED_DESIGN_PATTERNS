from proxies import InverterProxy, RouterProxy
from MediatorManager import EnergyManager
from time import sleep

def main():
    inverter_proxy = InverterProxy()
    router_proxy = RouterProxy()
    energy_manager = EnergyManager(inverter_proxy, router_proxy)

    running = True

    while running:
        status = inverter_proxy.get_status()

        log(status)

        battery_level = status["battery"]

        energy_manager.handle_battery_level(battery_level)

        sleep(3)

def log(status):
    print(f"[MAIN] {status}")

if __name__ == "__main__":
    print(f"Running application")
    main()