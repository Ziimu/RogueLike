BOSS + SCROLLID

(https://rogueliketutorials.com/tutorials/tcod/v2/part-7/)   ---Tehtud aga mouse over ei tööta. press V, 
https://rogueliketutorials.com/tutorials/tcod/v2/part-8/ --tehud
--> bug --> kollid saavad diagonaalis kah rünnata.
v = LOG
i = inventory.
d = drop items.
g = grab items from the floor

Siin on BOSS jee.  Tahax näidata mis ja kui palju HP-d on kollidel

 class MainGameEventHandler(EventHandler):c--> siit pooleni part10
-   def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
+   def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        action: Optional[Action] = Non