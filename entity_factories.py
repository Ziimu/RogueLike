from components.ai import HostileEnemy
from components import consumable
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
   fighter=Fighter(hp=10, defense=0, power=3),
   inventory=Inventory(capacity=0),
)

troll = Actor(
   char="T",
   color=(0, 127, 0),
   name="TROLL",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=16, defense=1, power=4),
   inventory=Inventory(capacity=0),
)

confusion_scroll = Item(
   char="~",
   color=(207, 63, 255),
   name="Confusion Scroll",
   consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

health_potion = Item(
   char="!",
   color=(127, 0, 255),
   name="Health Potion",
   consumable=consumable.HealingConsumable(amount=4), #kui palju see healib
)

lightning_scroll = Item(
   char="~",
   color=(127, 0, 255),
   name="Lightning Scroll",
   consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

fireball_scroll = Item(
   char="~",
   color=(255, 128, 0),
   name="Fireball Scroll",
   consumable=consumable.FireballDamageConsumable(damage=4, radius=2),
)
#player = Entity(char="@", color=(0, 0, 0), name="PLayer", blocks_movement=True)

#orc = Entity(char="O", color=(0, 127, 0), name="Orc", blocks_movement=True) # 63, 127, 63
#troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True) # 0, 127, 0