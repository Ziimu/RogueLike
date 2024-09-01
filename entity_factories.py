from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
   char="@",
   color=(0, 0, 0),
   name="Player",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
   char="o",
   color=(0, 127, 0),
   name="Orc",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=10, defense=0, power=3),
)

troll = Actor(
   char="T",
   color=(0, 127, 0),
   name="Troll",
   ai_cls=HostileEnemy,
   fighter=Fighter(hp=16, defense=1, power=4),
)

#player = Entity(char="@", color=(0, 0, 0), name="PLayer", blocks_movement=True)

#orc = Entity(char="O", color=(0, 127, 0), name="Orc", blocks_movement=True) # 63, 127, 63
#troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True) # 0, 127, 0