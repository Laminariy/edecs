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
hero = Hero(name='Brave Knight', entity_type='HeroEntity')
```

Либо при объявлении:

```python
from edecs import Entity

class HeroEntity(Entity):
    default_entity_type = 'HeroEntity'
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

# System

# Event

# ComponentManager

# EntityManager

# SystemManager

# EventManager

# Engine
