import sys
sys.path.append('..')
import asyncio
from edecs import *
msg = message

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

        event.fire('HiEvent')
        msg.post('LogSystem', 'HelloMessage')

class LogSystem(System):

    def on_start(self):
        print('LogSystem started')
        event.subscribe(self, 'HiEvent', self.hi_event_handler)

    def hi_event_handler(self, ev_type, ev_data):
        print(ev_type, ev_data)

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

    def on_message(self, msg_id, msg_type):
        print(msg_id, msg_type)


def start():
    log_system = LogSystem()
    world.create_system(log_system)
    world.create_system(PlayerCreatorSystem())

    loop = asyncio.get_event_loop()

    async def game_loop():
        while True:
            world.async_update(loop)
            msg.async_update(loop)
            event.async_update(loop)
            await asyncio.sleep(1)

    loop.create_task(game_loop())

    loop.run_forever()


if __name__ == '__main__':
    start()
