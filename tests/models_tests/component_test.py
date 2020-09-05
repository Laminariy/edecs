import sys
sys.path.append('../..')
import doctest
from edecs import Component

def test():
    '''
        >>> health_component = Component(component_type='Health', max_health=10, health=10)
        >>> health_component
        <Component:Health; Entity:None>
        >>> print(health_component)
        {
            "max_health": 10,
            "health": 10
        }
        >>> health_component.health -= 3
        >>> print(health_component)
        {
            "max_health": 10,
            "health": 7
        }
    '''

    doctest.testmod()

if __name__ == '__main__':
    test()
