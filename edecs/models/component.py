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

    # TO DO: look __new__ function in tutorial (append __slots__)

    def __init__(self, component_type=None, **properties):
        self._type = component_type or self.default_component_type or \
                                                            type(self).__name__
        self._entity = None

        if self.defaults == {}:
            for key, value in properties.items():
                setattr(self, key, value)
        else:
            for key, value in self.defaults.items():
                setattr(self, key, properties.pop(key, value))

    def __repr__(self):
        # <Component:type; Enity:entity>
        return "<Component:{}; Entity:{}>".format(self._type,
                                            self._entity if self._entity is None
                                                        else self._entity.type)

    '''def __str__(self):
        # JSON
        pass'''


    def create(self, entity):
        if self.initialized then:
            # TO DO: raise error (component already exist(have entity))
            pass

        setattr(entity, self._type, self)

    def destroy(self):
        # TO DO: destroy component
        # TO DO: raise error if component is not exist (no entity)
        pass
