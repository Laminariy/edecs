class EntityManager():

    @property
    def entities(self):
        return self._entities

    @property
    def entity_types(self):
        return self._entity_types


    def __init__(self):
        self._entity_count = 0
        self._entities = []
        self._entity_types = {}

    def create_entity(self, entity):
        if entity in self._entities:
            pass
            # TO DO: Raise error (entity already exist)

        entity._id = self._entity_count
        entity._entity_manager = self
        self._entity_count+=1

        self._entities.append(entity)

        if self._entity_types.get(entity.type) is None:
            self._entity_types[entity.type] = {}
        self._entity_types[entity.type][entity.id] = entity

    def destroy_entity(self, entity):
        if entity not in self._entities:
            pass
            # TO DO: Raise error (entity already deleted)

        self._entities[entity.id] = None

        del self._entity_types[entity.type][entity.id]
        if self._entity_types[entity.type] == {}:
            del self._entity_types[entity.type]
