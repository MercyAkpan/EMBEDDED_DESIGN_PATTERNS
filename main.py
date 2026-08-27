from mediator_pattern.proxies import InverterProxy, RouterProxy
from mediator_pattern.MediatorManager import EnergyManager
from time import sleep
from polling_pattern import poller
from queueing_pattern.queue import MessageQueue
from observer_pattern.observers.Logger import Logger
from observer_pattern.subjects.subject1 import subject1

def main():
    inverter_proxy = InverterProxy()
    router_proxy = RouterProxy()
    energy_manager = EnergyManager(inverter_proxy, router_proxy)
    _poller = poller.Poller(inverter_proxy, router_proxy)
    queue = MessageQueue()
    logger = Logger()

    ProcessorTask = subject1()

    ProcessorTask.subscribe(energy_manager)
    ProcessorTask.subscribe(logger)

    running = True

    while running:
        status = _poller.poll()

        queue.insert(status)

        data = queue.remove()

        if data:
            ProcessorTask.insert(data)
        else:
            print(f"[MAIN] No Data...")
        # energy_manager.handle_status(status)

        sleep(2)


if __name__ == "__main__":
    print(f"Running application")
    main()
