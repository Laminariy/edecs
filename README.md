# EDECS
Event-driven Entity-Component-System engine

ECS-фреймворк на базе событий

---

## Установка

```
pip install edecs
```

## Краткий гайд

### Компонент (Component)

Небольшой набор данных, отвечающих за то или иное свойство сущности.

Пример:

```python
from edecs import Component

class HealthComponent(Component):
    defaults = {
        'max_hp': 10,
        'hp': 10
    }
```

Это компонент "здоровья" сущности. Он хранит в себе максимально допустимый и текущий уровень здоровья.

```python
from random import random
from edecs import Component

class AttackComponent(Component):
    defaults = {
        'damage': 1,
        'crit_damage': 3,
        'crit_chance': 0.3,
        'target': -1
    }
    
    def get_damage(self):
        if random() <= self.crit_chance:
            return self.crit_damage
        
        return self.damage
```

Компонент, отвечающий за данные об атаке. Здесь можно увидеть, как можно обращаться к данным внутри компонента - как к обычным атрибутам класса.

Так же мы добавили здесь функцию, которая, в зависимости от рандом-генератора возвращает нанесенный урон - обычный или критический. Однако нужно помнить, что компоненты - это просто данные, и не нужно прописывать в них какую либо сложную логику. В данном случае мы просто работаем с данными самого компонента и немного упрощаем дальнейшую работу, так что в этом нет ничего страшного.

### Сущность (Entity)

Контейнер для компонентов. Сам по себе ничего не представляет - это просто объект, знающий свой идентификатор, тип и имя. Чтобы добавить сущности свойство, необходимо добавить ей компоненты.

Пример:

```python
from edecs import Entity
from health_component import HealthComponent
from attack_component import AttackComponent

class Skeleton(Entity):
    default_components = {
        'health': HealthComponent(max_hp=5, hp=5)
        'attack': AttackComponent()
    }
```

Сущность, отображающая игрового персонажа - скелета. Мы добавили ей компонент здоровья, созданный на предыдущем шаге, и установили начальные значения для параметров. Так же мы добавили компонент атаки. Значения атрибутов остались по умолчанию теми же, что мы и указывали на предыдущем пункте.

```python
from edecs import Entity
from health_component import HealthComponent
from attack_component import AttackComponent

class Hero(Entity):
    default_components = {
        'health': HealthComponent(max_hp=20, hp=20)
        'attack': AttackComponent(damage=3, crit_damage=5, crit_chance=0.45)
    }
```

Сущность героя. Имеет те же компоненты, что и скелет, но измененные значения (Это же герой, он должен быть сильным!)

### Система (System)

Системы используются для реализации той или иной логики.


Пример:

```python
from edecs import System
from skeleton import Skeleton
from hero import Hero

class CombatSystem(System):
    def init(self):
        hero = Hero()
        skeleton = Skeleton()
        
        self.create_entity(hero)
        self.create_entity(skeleton)
        
        hero.attack.target = skeleton.id
        skeleton.attack.target = hero.id
        
    def update(self, dt):
        attack_components = self.component_manager.component_types['AttackComponent']
        health_components = self.component_manager.component_types['HealthComponent']
        
        for id, atk in enumerate(attack_components):
            target_id = atk.target
            
            if target_id == -1: break
            
            damage = atk.get_damage()
            health_components[target_id].hp -= damage
            
            self.send_event('AttackEvent', {'attacker_id':id, 'target_id':target_id, 'damage':damage})
            
            if health_components[target_id].hp <= 0:
                self.send_event('DeathEvent', {'id':target_id})
                
                atk.target = -1
                
                death_entity = self.entity_manager.entities[target_id]
                self.destroy_entity(death_entity)
```
