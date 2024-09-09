from components.ai import HostileEnemy, BossAI
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
   consumable=consumable.HealingConsumable(amount=10), #kui palju see healib
)

lightning_scroll = Item(
   char="~",
   color=(6, 25, 148),
   name="Lightning Scroll",
   consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
   char="~",
   color=(207, 63, 255),
   name="Confusion Scroll",
   consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
   char="~",
   color=(255, 128, 0),
   name="Fireball Scroll",
   consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

speed_potion = Item(
    char="!",
    color=(0, 100, 0),  # Dark green color
    name="Speed Potion",
    consumable=consumable.SpeedPotionConsumable(number_of_turns=2),
)
#player = Entity(char="@", color=(0, 0, 0), name="PLayer", blocks_movement=True)

#orc = Entity(char="O", color=(0, 127, 0), name="Orc", blocks_movement=True) # 63, 127, 63
#troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True) # 0, 127, 0