from copy import deepcopy
from .exceptions import *
from . import Entity


class World():
    ''' World class'''

    entities = [] # [id: entity]
    components = {} # {type: ent_id: comp_id: comp}
    systems = {} # {type: system}

    dead_entities = []

    @classmethod
    def create_system(world, system):
        if world.systems.get(system.type) is not None:
            raise SystemTypeAlreadyExists(system)

        if system.initialized:
            raise SystemAlreadyInitialized(system)

        world.systems[system.type] = system
        system.initialized = True

        system.on_start()


    @classmethod
    def delete_system(world, system):
        if world.systems.get(system.type) is None:
            raise SystemDoesNotExist(system)

        if not system.initialized:
            raise SystemIsNotInitialized(system)

        system.on_finish()

        world.systems.pop(system.type)
        system.initialized = False

    @classmethod
    def create_entity(world, entity=None):
        if entity is None:
            entity = Entity()

        if entity.initialized:
            raise EntityAlreadyExists(entity)

        ent_id = -1

        if len(world.dead_entities) > 0:
            ent_id = world.dead_entities.pop(0)
            world.entities[ent_id] = entity

        else:
            ent_id = len(world.entities)
            world.entities.append(entity)

        entity.id = ent_id
        entity.initialized = True

        for comp_id, component in entity.default_components.items():
            component = deepcopy(component)
            world.add_component(entity, comp_id, component)

        return entity

    @classmethod
    def get_entity(world, entity_id):
        if entity_id is None or entity_id >= len(world.entities) or entity_id < 0:
            return None

        return world.entities[entity_id]

    @classmethod
    def get_entities(world):
        for entity in world.entities:
            yield entity

    @classmethod
    def delete_entity(world, entity):
        if isinstance(entity, int):
            entity_id = entity
            entity = world.get_entity(entity)

            if entity is None:
                raise EntityDoesNotExist(entity_id)

        elif world.get_entity(entity.id) is None:
            raise EntityDoesNotExist(entity)

        for component in entity.components.values():
            world.delete_component(component)

        world.entities[entity.id] = None
        world.dead_entities.append(entity.id)
        entity.id = None
        entity.initialized = False

    @classmethod
    def add_component(world, entity, component_id, component):
        if isinstance(entity, int):
            entity_id = entity
            entity = world.get_entity(entity)

            if entity is None:
                raise EntityDoesNotExist(entity_id)

        elif world.get_entity(entity.id) is None:
            raise EntityDoesNotExist(entity)

        if component.initialized:
            raise ComponentAlreadyHaveEntity(component)

        if world.components.get(component.type) is None:
            world.components[component.type] = {}

        type_components = world.components[component.type]

        if type_components.get(entity.id) is None:
            type_components[entity.id] = {}

        entity_type_components = type_components[entity.id]
        entity_type_components[component_id] = component

        component.id = component_id
        component.entity = entity
        entity.components[component_id] = component


    @classmethod
    def get_component(world, entity, component_id):
        if isinstance(entity, int):
            entity_id = entity
            entity = world.get_entity(entity)

            if entity is None:
                raise EntityDoesNotExist(entity_id)

        elif world.get_entity(entity.id) is None:
            raise EntityDoesNotExist(entity)

        return entity.components.get(component_id)

    @classmethod
    def get_components(world, component_type=None):
        result = world.components.get(component_type)

        if result is None:
            return []

        for component in result.values().values():
            yield component

    @classmethod
    def delete_component(world, component):
        if not component.initialized:
            raise ComponentHasNoEntity(component)

        entity = component.entity

        if world.get_entity(entity.id) is None:
            raise EntityDoesNotExist(entity)

        del entity.components[component.id]
        del world.components[component.type][entity.id][component.id]

        if len(world.components[component.type][entity.id]) == 0:
            del world.components[component.type][entity.id]

        if len(world.components[component.type]) == 0:
            del world.components[component.type]

        component.id = None
        component.entity = None

    @classmethod
    def update_systems(world):
        for system in world.systems.values():
            system.on_update()
