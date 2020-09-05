from copy import deepcopy


class Entity():
    '''Base entity class'''

    __slots__ = ['_type', '_id', '_name', '_components',
                 '_entity_manager', '_component_manager']

    default_entity_type = None
    default_components = {}


    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def components(self):
        return self._components

    @property
    def initialized(self):
        return self._entity_manager and self._component_manager


    def __init__(self, name, entity_type=None):
        self._type = entity_type or self.default_entity_type or \
                                                            type(self).__name__

        self._id = 'no_id'
        self._name = name
        self._components = deepcopy(self.default_components)

        self._entity_manager = None
        self._component_manager = None

    def __repr__(self):
        return "<Entity:{}; {}:{}>".format(self._type, self._name, self._id)

    def __str__(self):
        ent = "<Entity:{}; {}:{}>".format(self._type, self._name, self._id)
        components = self._components
        # TO DO: return repr of component
        return "{}\n{}".format(ent, components)

    def __getitem__(self, key):
        return self._components[key]

    def __setitem__(self, key, value):
        # TO DO: component initializing if managers is added
        # TO DO: check if component already have entity (already exist)
        self._components[key] = value

    def __getattr__(self, key):
        if key in super().__getattribute__('__slots__'):
            return super().__getattr__(key)
        else:
            return self._components[key]

    def __setattr__(self, key, value):
        # TO DO: component initializing if managers is added
        # TO DO: check if component already have entity (already exist)
        if key in super().__getattribute__('__slots__'):
            super().__setattr__(key, value)
        else:
            self._components[key] = value


    def create(self, entity_manager, component_manager):
        self._entity_manager = entity_manager
        self._component_manager = component_manager
        # TO DO: raise error if entity already exist (initialized)
        # TO DO: add entity and components into managers

    def destroy(self):
        # TO DO: destroy entity and all components
        # TO DO: raise error if entity is not initialized
        pass
