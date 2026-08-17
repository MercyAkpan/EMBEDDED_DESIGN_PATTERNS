from observers import observer1, observer2, observer3
from subjects import subject1
import random, time

if __name__ == "__main__":
    SensorQueue = subject1.subject1()
    LoggingObserver = observer1.observer1(SensorQueue)
    LoggingObserver.install()

    DashboardObserver = observer2.observer2(SensorQueue)
    DashboardObserver.install()

    AlertObserver = observer3.observer3(SensorQueue)
    AlertObserver.install()

    #insert logic
    for _ in range(3):
        data = {
            "reading": round(random.uniform(60.0, 100.0), 2),
            "timestamp": time.time()
        }

        SensorQueue.insert(data)
        time.sleep(1)

    LoggingObserver.deinstall()
    DashboardObserver.deinstall()
    AlertObserver.deinstall()
    