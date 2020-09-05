class System():
    '''Base system class'''

    __slots__ = ['_type', '_entity_manager', '_component_manager',
                 '_system_manager', '_event_manager']

    default_system_type = None


    @property
    def type(self):
        return self._type


    def __init__(self, system_type=None):
        self._type = system_type or default_system_type or type(self).__name__

        self._entity_manager = None
        self._component_manager = None
        self._system_manager = None
        self._event_manager = None


    def send(self, event_type):
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

        # TO DO: add system into system manager

        init()

    def destroy(self):
        # TO DO: system destroy (and unsubscribing all events)
        final()


    def init(self):
        pass

    def final(self):
        pass
