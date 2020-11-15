import sys
sys.path.append('../..')
import doctest
from edecs import (Entity, Component)

def test():
    '''
        >>> player = Entity("player")
        >>> health = Component("HealthComponent", max_hp=10, hp=10)
        >>> player.health = health
        >>> print(player['health'])
        {
            "max_hp": 10,
            "hp": 10
        }
        >>> player
        <Entity:Entity; player:no_id>
        >>> print(player)
        <Entity:Entity; player:no_id>
        {'health': <Component:HealthComponent; Entity:Entity>}
        >>> print(player.id)
        no_id
        >>> print(player.type)
        Entity
        >>> player._id = 5
        >>> print(player.id)
        5
        >>> player['health'].hp = 7
        >>> print(player['health'].hp)
        7

        >>> class Skeleton(Entity):
        ...     default_entity_type = "Skeleton-Archer"
        ...     default_components = {'health': Component("HealthComponent", max_hp=10, hp=10)}
        ...

        >>> skeleton = Skeleton("skeleton-001")
        >>> print(skeleton)
        <Entity:Skeleton-Archer; skeleton-001:no_id>
        {'health': <Component:HealthComponent; Entity:Skeleton-Archer>}
        >>> print(skeleton.health.hp)
        10
    '''

    doctest.testmod()

if __name__ == "__main__":
    test()
