class Message():
    '''class for sending messages'''

    class _Message():
        '''inner class for message'''
        def __init__(self, sender, adress, msg_type, msg_data={}):
            self.sender = sender
            self.adress = adress
            self.message_type = msg_type
            self.message_data = msg_data


    def __init__(self):
        self.message_queue = []
        self.subscribers = {} # {adress: {msg_type, fn}}


    def get_message_queue(self):
        return self.message_queue

    def get_subscribers(self, adress):
        pass


    @staticmethod
    def subscribe(self, msg_type, fn):
        pass

    @staticmethod
    def unsubscribe(self, msg_type, fn):
        pass

    @staticmethod
    def post(self, adress, msg_type, msg_data):
        pass
