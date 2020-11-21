from time import time
from .models import Event
from .managers import (EntityManager, ComponentManager,
                       SystemManager, EventManager)

class Engine():

    @property
    def entity_manager(self):
        return self._entity_manager

    @property
    def component_manager(self):
        return self._component_manager

    @property
    def system_manager(self):
        return self._system_manager

    @property
    def event_manager(self):
        return self._event_manager

    def __init__(self):
        self._entity_manager = EntityManager()
        self._component_manager = ComponentManager()
        self._system_manager = SystemManager()
        self._event_manager = EventManager()

        self.last_update = time()

    def create_system(self, system):
        system.create(self._entity_manager, self._component_manager,
                      self._system_manager, self._event_manager)

    def destroy_system(self, system):
        system.destroy()

    def generate_input(self, event_type='InputEvent', data=None):
        event = Event(event_type, data)

        self._event_manager.add_event(event)

    def send_input(self, event):
        self._event_manager.add_event(event)

    def get_output(self):
        return self._event_manager.engine_events

    def update(self):
        systems = self.system_manager.system_types

        for system in systems.values():
            system.update(time()-self.last_update)

        self.last_update = time()

        while not self.event_manager.empty:
            self.event_manager.update_events()
