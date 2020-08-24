class Entity():
    '''
        Сущность. Знает свой айди, имя и компоненты. Можно наследовать и
        задавать тип и компоненты. Можно создать экземпляр "чистой" сущности.
        1) Инициализируется через менеджер или встроенную функцию
        2) При инициализации сущности инициализируются все подключенные компо-
                                                                          ненты.
        3) Компоненты хранятся в виде объектов
        4) Инициализация - значит привязка к менеджерам
    '''
    __slots__ = ['_type', '_id', '_name', '_components',
                 '_entity_manager', '_component_manager']

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


    def __init__(self, name, type="Entity"):
        self._type = type
        self._id = 'no_id'
        self._name = name
        self._components = {}

    def __repr__(self):
        return "<Entity:{}, {}:{}>".format(self._type, self._name, self._id)

    def __str__(self):
        ent = "<Entity:{}, {}:{}>".format(self._type, self._name, self._id)
        components = self._components
        # TO DO: return repr of component
        return "{}\n{}".format(ent, components)

    def __getitem__(self, key):
        return self._components[key]

    def __setitem__(self, key, value):
        # TO DO: component initializing if managers is added
        self._components[key] = value

    def __getattr__(self, key):
        if key in super().__getattribute__('__slots__'):
            return super().__getattr__(key)
        else:
            return self._components[key]

    def __setattr__(self, key, value):
        # TO DO: component initializing if managers is added
        if key in super().__getattribute__('__slots__'):
            super().__setattr__(key, value)
        else:
            self._components[key] = value


    def init(self, entity_manager, component_manager):
        self._entity_manager = entity_manager
        self._component_manager = component_manager

        # TO DO: add entity and components into managers
