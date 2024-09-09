from __future__ import annotations

from typing import TYPE_CHECKING

import tcod
import tcod.constants

from tcod.console import Console
from tcod.map import compute_fov

import exceptions
from input_handlers import MainGameEventHandler
from message_log import MessageLog
from render_functions import render_bar, render_names_at_mouse_location
import color

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap
    from input_handlers import EventHandler

class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.event_handler: EventHandler = MainGameEventHandler(self)
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # ignore impossible action exceptions from AI

    def update_fov(self) -> None:
        # Recompute the visible area based on the players point of view.
        self.game_map.visible[:] = tcod.map.compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=5,
            light_walls=False,
            algorithm=tcod.constants.FOV_SYMMETRIC_SHADOWCAST,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible
    """
    def handle_events(self, event: tcod.event.Event) -> None:
        action = self.event_handler.dispatch(event)

        if action is None:
            return

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.message_log.add_message(exc.args[0], color.impossible)
            return

        if hasattr(self.player, 'speed_turns') and self.player.speed_turns > 0:
            # Player gets an extra action when under speed effect
            self.player.speed_turns -= 1 #1
            if self.player.speed_turns == 0:
                self.message_log.add_message(
                    "The speed potion's effect has worn off.",
                    color.status_effect_applied
                )
            else:
                # Extra action
                try:
                    action = self.event_handler.dispatch(event)
                    if action:
                        action.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible actions for the extra move

        self.handle_enemy_turns()
        self.update_fov()
    """
    
    def handle_events(self, event: tcod.event.Event) -> None:
        action = self.event_handler.dispatch(event)

        if action is None:
            return

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.message_log.add_message(exc.args[0], color.impossible)
            return

        if hasattr(self.player, 'speed_turns') and self.player.speed_turns > 0:
            # Player gets an extra action when under speed effect
            # Extra action
            try:
                action = self.event_handler.dispatch(event)
                if action:
                    action.perform()
            except exceptions.Impossible:
                pass  # Ignore impossible actions for the extra move
            
            self.player.speed_turns -= 1
            if self.player.speed_turns == 0:
                self.message_log.add_message(
                    "The speed potion's effect has worn off.",
                    color.status_effect_applied
                )

        self.handle_enemy_turns()
        self.update_fov()

    def render(self, console: Console) -> None:
        self.game_map.render(console)
        
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)
        
        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )
        
        render_names_at_mouse_location(console=console, x=21, y=44, engine=self)

        # Render speed potion effect if active
        if hasattr(self.player, 'speed_turns') and self.player.speed_turns > 0:
            console.print(x=1, y=47, string=f"Speed Potion: {self.player.speed_turns} turns", fg=color.status_effect_applied)