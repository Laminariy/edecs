class Event():
    '''class for sending events'''

    class _Event():
        '''inner class for event'''
        def __init__(self, sender, event_type, event_data={}):
            self.sender = sender
            self.event_type = event_type
            self.event_data = event_data


    def __init__(self):
        self.event_queue = []
        self.subscribers = {} # {event_type: fn}


    def get_event_queue(self):
        return self.event_queue

    def get_subscribers(self, event_type):
        pass


    @staticmethod
    def subscribe(self, event_type='All', fn=None):
        pass

    @staticmethod
    def unsubscribe(self, event_type='All', fn=None):
        pass

    @staticmethod
    def fire(self, event_type, event_data={}):
        pass
