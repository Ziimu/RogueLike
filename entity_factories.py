from entity import Entity

player = Entity(char="@", color=(0, 0, 0), name="PLayer", blocks_movement=True)

orc = Entity(char="O", color=(0, 127, 0), name="Orc", blocks_movement=True) # 63, 127, 63
troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True) # 0, 127, 0