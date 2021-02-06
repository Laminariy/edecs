import sys
sys.path.append('..')
from time import sleep
from edecs import *
world = World

class HealthComponent(Component):

    defaults = {
        'max_hp': 10,
        'hp': 10
    }

class DamageComponent(Component):

    defaults = {
        'damage': 3
    }


class PlayerEntity(Entity):

    default_components = {
        'health': HealthComponent(max_hp=20, hp=20),
        'damage': DamageComponent()
    }


class PlayerCreatorSystem(System):

    def on_start(self):
        world.create_entity(PlayerEntity())
        world.create_entity(PlayerEntity())
        world.create_entity(PlayerEntity())

        tst = PlayerEntity()
        world.create_entity(tst)
        world.delete_entity(tst)

class LogSystem(System):

    def on_start(self):
        print('LogSystem started')

    def on_update(self):
        print('LogSystem updated')

        print('Entities:')
        for entity in world.get_entities():
            print(entity)
            world.delete_entity(entity)

        print('Components:')
        for component in world.get_components():
            print(component)
            world.delete_component(component)

        print(world.entities)
        print(world.components)
        print(world.systems)
        print(world.dead_entities)
        print(world.components_del_queue)

    def on_finish(self):
        print('LogSystem finished')


def start():
    log_system = LogSystem()
    world.create_system(log_system)
    world.create_system(PlayerCreatorSystem())

    while True:
        sleep(1)
        world.update()


if __name__ == '__main__':
    start()
