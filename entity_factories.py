from components.ai import HostileEnemy, BossAI
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
   char="@",
   color=(0, 0, 0),
   name="Player",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=30, defense=2, power=5),
   inventory=Inventory(capacity=10), #INVENTORY CAPACITY
)

orc = Actor(
   char="o",
   color=(0, 127, 0),
   name="ORC",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=5, defense=0, power=3),
   inventory=Inventory(capacity=0),
)

troll = Actor(
   char="T",
   color=(0, 127, 0),
   name="TROLL",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=5, defense=0, power=3),
   inventory=Inventory(capacity=0),
)

boss = Actor(
    char="@",
    color=(255, 0, 0),  # Color can be adjusted as desired
    name="Boss",
    ai_cls=BossAI,
    fighter=Fighter(hp=10, defense=0, power=3),  # Stronger stats for the boss
    inventory=Inventory(capacity=0),
)

health_potion = Item(
   char="!",
   color=(127, 0, 255),
   name="Health Potion",
   consumable=HealingConsumable(amount=4), #kui palju see healib
)

#player = Entity(char="@", color=(0, 0, 0), name="PLayer", blocks_movement=True)

#orc = Entity(char="O", color=(0, 127, 0), name="Orc", blocks_movement=True) # 63, 127, 63
#troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True) # 0, 127, 0