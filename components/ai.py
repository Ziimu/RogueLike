from __future__ import annotations

from typing import List, Tuple, TYPE_CHECKING

import numpy as np
import tcod

from actions import Action, MeleeAction, MovementAction, WaitAction

if TYPE_CHECKING:
    from entity import Actor

class BaseAI(Action):
    entity: Actor
    
    def perform(self) -> None:
        raise NotImplementedError()
    
    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        #compute and return a path to target, if there is no valid path return an empty list.
        
        cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)
        
        for entity in self.entity.gamemap.entities:
            #check that an entity blovks movemenet and the cost isnt zero
            if entity.blocks_movement and cost[entity.x, entity.y]:
                # Add to the cost of a blocked position.
                # A lower number means more enemies will crowd behind each other in
                # hallways.  A higher number means enemies will take longer paths in
                # order to surround the player.
                cost[entity.x, entity.y] += 10
                
        graph = tcod.path.SimpleGraph(cost=cost, cardinal=2, diagonal=3)
        pathfinder = tcod.path.Pathfinder(graph)
        
        pathfinder.add_root((self.entity.x, self.entity.y))
        
        path: List[list[int]] = pathfinder.path_to((dest_x, dest_y))[1:].tolist()
        
        return [(index[0], index[1]) for index in path]
    
class HostileEnemy(BaseAI):
   def __init__(self, entity: Actor):
       super().__init__(entity)
       self.path: List[Tuple[int, int]] = []

   def perform(self) -> None:
       target = self.engine.player
       dx = target.x - self.entity.x
       dy = target.y - self.entity.y
       distance = max(abs(dx), abs(dy))  # Chebyshev distance.

       if self.engine.game_map.visible[self.entity.x, self.entity.y]:
           if distance <= 1:
               return MeleeAction(self.entity, dx, dy).perform()

           self.path = self.get_path_to(target.x, target.y)

       if self.path:
           dest_x, dest_y = self.path.pop(0)
           return MovementAction(
               self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
           ).perform()

       return WaitAction(self.entity).perform()


class BossAI(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.stationary_turns = 20  # The number of turns the boss stays in place
        self.path: List[Tuple[int, int]] = []  # Initialize path for the boss

    def perform(self) -> None:
        # If the boss still has stationary turns left, decrement and do nothing
        if self.stationary_turns > 0:
            self.stationary_turns -= 1
            return WaitAction(self.entity).perform()

        # After stationary turns are over, boss should actively seek the player
        target = self.engine.player
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance

        if distance <= 1:
            # If the player is within attack range, perform a melee attack
            return MeleeAction(self.entity, dx, dy).perform()
        else:
            # Calculate path towards the player regardless of visibility
            self.path = self.get_path_to(target.x, target.y)

        if self.path:
            # Follow the path to the player
            dest_x, dest_y = self.path.pop(0)
            return MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()

        # If no path is found or the player is unreachable, wait
        return WaitAction(self.entity).perform()