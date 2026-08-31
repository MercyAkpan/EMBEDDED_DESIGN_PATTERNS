from single_event_receptor_pattern.event import EventType, SystemState

class EnergyStateMachine:

    def __init__(self):
        self.__state = SystemState.NORMAL

    def event_dispatch(self, event):
        # TODO: Later add in current state checking, and exiting current state
        if event.event_type == EventType.BATTERY_CRITICAL:
            self.__enter_critical_mode()
        elif event.event_type == EventType.BATTERY_LOW:
            self.__enter_low_power_mode()
        elif event.event_type == EventType.BATTERY_NORMAL:
            self.__enter_normal_mode()
        
    def __enter_critical_mode(self):
        self.__state = SystemState.CRITICAL_SAVING
        print(f"[STATE_MACHINE] System in CRITICAL SAVING Mode..")

    def __enter_low_power_mode(self):
            self.__state = SystemState.LOW_POWER
            print(f"[STATE_MACHINE] System in LOW POWER Mode..")

    def __enter_normal_mode(self):
            self.__state = SystemState.NORMAL
            print(f"[STATE_MACHINE] System in NORMAL Mode..")
    