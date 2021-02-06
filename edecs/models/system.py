class System():
    '''Base system class'''

    def __init__(self):
        self.type = type(self).__name__
        self.initialized = False

    def __repr__(self):
        return "<System {}>".format(self.type)

    def __str__(self):
        return "<System {}>".format(self.type)


    def on_start(self):
        pass

    def on_update(self):
        pass

    def on_finish(self):
        pass


    def on_message(self, msg_type, msg_data):
        pass
