class Event():
    '''class for sending events'''

    events = [] # [(ev_type, ev_data), (ev_type, ev_data)]
    subscribers = {} # {event_type: [sub1, sub2, sub3]}


    @classmethod
    def update(event):
        while len(event.events) > 0:
            ev = event.events.pop(0)
            event_type, event_data = ev[0], ev[1]
            subscribers = event.subscribers.get('_all', []) + event.subscribers.get(event_type, [])

            for subscriber in subscribers:
                subscriber(event_type, event_data)


    @classmethod
    def subscribe(event, event_type, fn):
        if event.subscribers.get(event_type) is None:
            event.subscribers[event_type] = []

        if fn not in event.subscribers[event_type]:
            event.subscribers[event_type].append(fn)

    @classmethod
    def unsubscribe(event, event_type, fn):
        if event.subscribers.get(event_type) is None:
            return

        if fn not in event.subscribers[event_type]:
            return

        event.subscribers[event_type].remove(fn)

        if len(event.subscribers[event_type]) == 0:
            del event.subscribers[event_type]

    @classmethod
    def fire(event, event_type, event_data=None):
        event.events.append((event_type, event_data))
