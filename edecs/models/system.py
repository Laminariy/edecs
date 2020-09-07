from event import Event


class System():
    '''Base system class'''

    __slots__ = ['_type', '_entity_manager', '_component_manager',
                 '_system_manager', '_event_manager']

    default_system_type = None


    @property
    def type(self):
        return self._type

    @property
    def initialized(self):
        return self._entity_manager and self._component_manager and \
               self._system_manager and self._event_manager


    def __init__(self, system_type=None):
        self._type = system_type or default_system_type or type(self).__name__

        self._entity_manager = None
        self._component_manager = None
        self._system_manager = None
        self._event_manager = None

        self._subscribed_functions = []


    def create_entity(self, entity):
        if not self.initialized:
            pass
            # TO DO: Raise error (system isn't initialized)

        entity.create(self._entity_manager, self._component_manager)

    def send(self, event_type, data):
        if not self.initialized:
            pass
            # TO DO: Raise error (system isn't initialized)

        event = Event(event_type, data)
        self._event_manager.add_event(event)

    def subscribe(self, fn, event_type):
        # TO DO: decorator
        if not self.initialized:
            pass
            # TO DO: Raise error (system isn't initialized)

        self._subscribed_functions.append((fn, event_type))
        self._event_manager.subscribe(fn, event_type)

    def unsubscribe(self, fn, event_type):
        if not self.initialized:
            pass
            # TO DO: Raise error (system isn't initialized)

        self._subscribed_functions.remove((fn, event_type))
        self._event_manager.unsubscribe(fn, event_type)

    def create(self, entity_manager, component_manager,
                                                system_manager, event_manager):
        if self.initialized:
            pass
            # TO DO: Raise error (system already created)

        self._entity_manager = entity_manager
        self._component_manager = component_manager
        self._system_manager = system_manager
        self._event_manager = event_manager

        self._system_manager.create_system(self)

        init()

    def destroy(self):
        final()

        if not self.initialized:
            pass
            # TO DO: Raise error (system isn't initialized)

        for subscriber in self._subscribed_functions:
            self._event_manager.unsubscribe(subscriber[0], subscriber[1])
        self._system_manager.destroy_system(self)

        self._entity_manager = None
        self._component_manager = None
        self._system_manager = None
        self._event_manager = None


    def init(self):
        pass

    def final(self):
        pass
