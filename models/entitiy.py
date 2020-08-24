class Entity():
    '''
        Сущность. Знает свой айди, имя и компоненты. Можно наследовать и
        задавать тип и компоненты. Можно создать экземпляр "чистой" сущности.
        1) Инициализируется через менеджер или встроенную функцию
        2) При инициализации сущности инициализируются все подключенные компо-
                                                                          ненты.
        3) Компоненты хранятся в виде объектов
        4) Инициализация - значит привязка к менеджерам

        >>> player = Entity("player")
        >>> player.health = 10
        >>> print(player['health'])
        10
        >>> player
        <Entity:Entity, player:no_id>
        >>> print(player)
        <Entity:Entity, player:no_id>
        {} # components here
    '''
    __slots__ = ['type', 'id', 'name', 'components',
                 'entity_manager', 'component_manager']

    type = "Entity"
    components = {}

    def __init__(self, name):
        self.type = type
        self.id = "no_id"
        self.name = name
        self.components = components

        del type, components

    def __repr__(self):
        return "<Entity{}, {}:{}>".format(self.type, self.name, self.id)

    def __str__(self):
        ent = "<Entity{}, {}:{}>".format(self.type, self.name, self.id)
        components = self.components
        # TO DO: return repr of component
        return "{}\n{}".format(ent, components)

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __getattr__(self, key):
        pass

    def __settatr__(self, key, value):
        pass

    def init(self, entity_manager, component_manager):
        self.entity_manager = entity_manager
        self.component_manager = component_manager

        # TO DO: add entity and components into managers
