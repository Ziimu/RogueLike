from typing import Optional, Set
import tcod.event
from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self):
        super().__init__()
        self.pressed_keys: Set[int] = set()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        return EscapeAction()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        key = event.sym

        # Check if ESCAPE is pressed to exit the game
        if key == tcod.event.K_ESCAPE:
            return EscapeAction()

        # Otherwise, add the key to the set of pressed keys
        self.pressed_keys.add(key)
        return self.handle_movement()

    def ev_keyup(self, event: tcod.event.KeyUp) -> Optional[Action]:
        # Remove the key from the set when released
        self.pressed_keys.discard(event.sym)
        return None

    def handle_movement(self) -> Optional[Action]:
        dx, dy = 0, 0

        if tcod.event.K_UP in self.pressed_keys:
            dy -= 1
        if tcod.event.K_DOWN in self.pressed_keys:
            dy += 1
        if tcod.event.K_LEFT in self.pressed_keys:
            dx -= 1
        if tcod.event.K_RIGHT in self.pressed_keys:
            dx += 1

        # If there's any movement, return a MovementAction
        if dx != 0 or dy != 0:
            return MovementAction(dx=dx, dy=dy)

        # Return None if no movement was detected
        return None
