import sys
sys.path.append('../..')
import doctest
from models.entity import Entity

def test():
    '''
        >>> player = Entity("player")
        >>> player.health = 10
        >>> print(player['health'])
        10
        >>> player
        <Entity:Entity, player:no_id>
        >>> print(player)
        <Entity:Entity, player:no_id>
        {'health': 10}
        >>> print(player.id)
        no_id
        >>> print(player.type)
        Entity
        >>> player._id = 5
        >>> print(player.id)
        5
    '''

    doctest.testmod()

if __name__ == "__main__":
    test()
