class System():

    __slots__ = ['_type']

    default_system_type = None

    def __init__(self, system_type=None):
        self._type = system_type or default_system_type or type(self).__name__

        self._entity_manager = None
        self._component_manager = None
        self._system_manager = None
        self._event_manager = None


    def send_event(self, event_type):
        pass

    def subscribe(self, fn, event_type):
        pass

    def unsubscribe(self, fn, event_type):
        pass

    def create(self, entity_manager, component_manager,
                                                system_manager, event_manager):
        self._entity_manager = entity_manager
        self._component_manager = component_manager
        self._system_manager = system_manager
        self._event_manager = event_manager

        init()

    def destroy(self):
        # TO DO: system destroy (and unsubscribing all events)
        final()


    def init(self):
        pass

    def final(self):
        pass
