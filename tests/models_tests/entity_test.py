import sys
sys.path.append('../..')
import doctest
from edecs import Entity

def test():
    '''
        >>> player = Entity("player")
        >>> player.health = 10
        >>> print(player['health'])
        10
        >>> player
        <Entity:Entity; player:no_id>
        >>> print(player)
        <Entity:Entity; player:no_id>
        {'health': 10}
        >>> print(player.id)
        no_id
        >>> print(player.type)
        Entity
        >>> player._id = 5
        >>> print(player.id)
        5
        >>> player['health'] = 7
        >>> print(player['health'])
        7

        >>> class Skeleton(Entity):
        ...     default_entity_type = "Skeleton-Archer"
        ...     default_components = {'health': 10}
        ...

        >>> skeleton = Skeleton("skeleton-001")
        >>> print(skeleton)
        <Entity:Skeleton-Archer; skeleton-001:no_id>
        {'health': 10}
        >>> print(skeleton.health)
        10
    '''

    doctest.testmod()

if __name__ == "__main__":
    test()
