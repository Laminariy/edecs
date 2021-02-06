class System():
    '''Base system class'''

    def __init__(self):
        self.type = type(self).__name__
        self.initialized = False


    def on_start(self):
        pass

    def on_update(self):
        pass

    def on_finish(self):
        pass


    def on_message(self, sender, msg_type, msg_data):
        pass

    def on_event(self, sender, event_type, event_data):
        pass
