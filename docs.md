# Component

## Атрибуты

### `type`

Тип компонента.

Задается либо при создании:

```python
health_component = HealthComponent(component_type='HealthComponent')
```

Либо при объявлении:

```python
from edecs import Component

class HealthComponent(Component):
    default_component_type = 'HealthComponent'
```

По умолчанию, если не указывать тип, то будет использоваться имя класса.

### `entity`

Указывает на сущность, к которой прикреплен компонент. None, если компонент не имеет сущности.

### `initialized`

True, если закреплен за сущностью. Иначе - False.

## Варианты создания

### Через наследование:

```python
from edecs import Component

class HealthComponent(Component):
    defaults = {
        'max_hp': 10,
        'hp': 10
        }
```

#### Модификация

Теперь, при создании экземпляра HealthComponent, мы можем изменять значения его атрибутов.

```python
health = HealthComponent(max_hp=20, hp=20)
```

### Создание в коде:

```python
from edecs import Component

def create_health_component(max_hp, hp):
    health_component = Component(component_type='HealthComponent', max_hp=max_hp, hp=hp)
    return health_component
```

# Entity

## Атрибуты

### `type`

Тип сущности.

Задается либо при создании:

```python
hero = Hero(name='Brave Knight', entity_type='Hero')
```

Либо при объявлении:

```python
from edecs import Entity

class Hero(Entity):
    default_entity_type = 'Hero'
```

По умолчанию, если не указывать тип, то будет использоваться имя класса.

### `id`

Идентификатор сущности. Уникален для каждой сущности. Присваивается при добавлении сущности в "мир" (при создании через system.create_entity())

### `name`

Имя сущности. Обязательный параметр при создании объекта конкретной сущности.

```python
hero = Hero('Brave Knight')
```

### `components`

Словарь компонентов сущности.

### `initialized`

True, если сущность создана и находится в "мире". Иначе False.

## Варианты создания

### Через наследование:

```python
from edecs import Entity
from components import HealthComponent

class Hero(Entity):
    default_components = {
        'health': HealthComponent()
    }

```

```python
hero = Hero('Brave Knight')
```

### Создание в коде

```python
from edecs import Entity
from components import HealthComponent

def create_hero():
    hero = Entity(name='Brave Knight', entity_type='Hero')
    hero.health = HealthComponent()
    # hero['health'] = HealthComponent() - аналогичная запись
    
    return hero
```

# Event

## Атрибуты

### `type`

Тип события.

Задается либо при создании:

```python
attack_event = AttackEvent(event_type='AttackEvent')
```

Либо при объявлении:

```python
from edecs import Event

class AttackEvent(Event):
    default_event_type = 'AttackEvent'
```

По умолчанию, если не указывать тип, то будет использоваться имя класса.

### `sysname`

Тип системы, которая сгенерировала событие, обязательный атрибут.

### `data`

Словарь. Данные, передаваемые вместе с событием.

Задается либо при создании:

```python
attack_event = AttackEvent(event_type='AttackEvent', data={'damage':5})
```

```python
attack_event = AttackEvent(event_type='AttackEvent', damage=5)
```

Либо при объявлении:

```python
from edecs import Event

class AttackEvent(Event):
    default_event_data = {
        'damage': 5
    }
```

# System

## Атрибуты

### `type`

Тип системы.

Задается либо при создании:

```python
combat_system = CombatSystem(system_type='CombatSystem')
```

Либо при объявлении:

```python
from edecs import System

class CombatSystem(System):
    default_system_type = 'CombatSystem'
```

По умолчанию, если не указывать тип, то будет использоваться имя класса.

### `initialized`

True, если система была создана через Engine, и существует в "мире". Иначе False.

### `entity_manager`

Объект менеджера сущностей.

### `component_manager`

Объект менеджера компонентов.

### `system_manager`

Объект менеджера сущностей.

### `event_manager`

Объект менеджера событий.

## Методы

### `create_entity(entity)`

Добавляет сущность в "мир". 

`entity` - объект сущности.

### `destroy_entity(entity)`

Удаляет сущность из "мира".

`entity` - объект сущности.

### `generate_event(event_type[, data])`

Генерирует и отправляет событие.

`event_type` - строка, тип события.

`data` - необязательный параметр. Словарь данных, которые нужно передать вместе с событием.

### `send_event(event)`

Отправляет событие.

`event` - объект события.

### `generate_engine_event(event_type[, data])`

Генерирует и отправляет событие в движок.

`event_type` - строка, тип события.

`data` - необязательный параметр. Словарь данных, которые нужно передать вместе с событием.

### `send_engine_event(event)`

Отправляет событие в движок.

`event` - объект события.

### `subscribe(fn, event_type)`

Подписывает функцию на событие.

`fn` - функция, которую необходимо подписать на событие. Функция должна принимать только один параметр - event.

`event_type` - строка, типо события, на которое необходимо подписать функцию.

### `unsubscribe(fn, event_type)`

Отписывает функцию от события.

`fn` - функция, которую необходимо отписать.

`event_type` - строка, тип события, от которого нужно отписать функцию.

### `init()`

Функция вызываетя один раз при добавлении системы в "мир".

### `update(dt)`

Функция вызывается каждый проход игрового цикла. 

`dt` - float, время в секундах, прошедшее с последнего обновления.

### `final()`

Функция вызывается один раз при удалении системы из "мира".

# ComponentManager

## Атрибуты

### `components`

Список всех существующих компонентов.

### `component_types`

Двумерный словарь. Ключи внешнего - тип компонента. Ключи вложенного - идентификатор сущности. Значения - объект компонента.

`{'component_type': {'entity_id': Component()}}`

## Методы

### `component_exists(component_type, entity_id)`

Возвращает True, если у сущности присутствует компонент заданного типа.

`component_type` - строка, тип компонента.

`entity_id` - число, идентификатор сущности.

# EntityManager

## Атрибуты

### `entities`

Список всех сущностей. Ключ - идентификатор сущности, значение - объект сущности.

### `entity_types`

Двумерный словарь. Ключи внешнего - тип сущности. Ключи вложенного - идентификатор сущности. Значения - объект сущности.

`{'entity_type': {'entity_id': Entity()}}`

## Методы

### `entity_exists(entity_id)`

Возвращает True, если сущность с указанным айди существует.

# SystemManager

## Атрибуты

### `system_types`

Словарь. Ключ - тип системы, значение - объект системы.

`{'system_type': System()}`

# EventManager

## Атрибуты

### `subscribers`

Словарь подписчиков на события. 

Ключ - тип события, значение - список подписанных функций.

`{'event_type': [fn1, fn2]}`

### `events`

Список событий, находящихся в очереди.

### `engine_events`

Список событий движка, находящихся в очереди.

### `empty`

True, если очередь событий пуста.

# Engine

## Атрибуты

### `entity_manager`

Объект менеджера сущностей.

### `component_manager`

Объект менеджера компонентов.

### `system_manager`

Объект менеджера сущностей.

### `event_manager`

Объект менеджера событий.

## Методы

### `create_system(system)`

Создает систему и запускает ее работу. Добавляет систему в "мир".

`system` - объект системы.

### `destroy_system(system)`

Удаляет систему, останавливает ее работу. Удаляет систему из "мира".

`system` - объект системы

### `generate_input([event_type, data])`

Генерирует и отправляет событие из движка в системы.

`event_type` - строка, тип события. По умолчанию 'InputEvent'

`data` - словарь с данными, которые необходимо передать вместе с событием.

### `send_input(event)`

Отправляет событие из движка в системы.

`event` - объект события.

### `get_output()`

Возвращает список событий, отправленных из систем движку.

### `update()`

Один проход игрового цикла. Вызывает метод update() у всех систем. Рассылает все события из очереди.
