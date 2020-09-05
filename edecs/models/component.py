import json


class Component():
    '''Base component class'''

    #__slots__ = ['_type', '_entity']

    default_component_type = None
    defaults = {}


    @property
    def type(self):
        return self._type

    @property
    def entity(self):
        return self._entity

    @property
    def initialized(self):
        return self._entity


    def __init__(self, component_type=None, **properties):
        self._type = component_type or self.default_component_type or \
                                                            type(self).__name__
        self._entity = None

        if self.defaults == {}:
            for key, value in properties.items():
                #setattr(self, key, value)
                self.defaults[key] = value

        for key, value in self.defaults.items():
            setattr(self, key, properties.pop(key, value))

    def __repr__(self):
        # <Component:type; Enity:entity>
        return "<Component:{}; Entity:{}>".format(self._type,
                                            self._entity if self._entity is None
                                                        else self._entity.type)

    def __str__(self):
        # JSON
        keys = self.defaults.keys()
        data = {}

        for key in keys:
            data[key] = getattr(self, key)

        json_string = json.dumps(data, indent=4)
        return json_string


    def create(self, entity):
        if self.initialized:
            # TO DO: raise error (component already exist(have entity))
            pass

        setattr(entity, self._type, self)

    def destroy(self):
        # TO DO: destroy component
        # TO DO: raise error if component is not exist (no entity)
        pass
