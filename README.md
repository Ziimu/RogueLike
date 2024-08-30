https://rogueliketutorials.com/tutorials/tcod/v2/part-4/ -tehtud
https://python-tcod.readthedocs.io/en/latest/tcod/map.html#tcod.map.compute_fov



random map töötab, liigub diagonaalis

def update_fov(self, algorithm: int = 2) -> None:
       """Recompute the visible area based on the players point of view."""
       self.game_map.visible[:] = compute_fov(
           self.game_map.tiles["transparent"],
           (self.player.x, self.player.y),
           radius=5,
           light_walls=False,
           algorithm=2,
           
           
       )

see copida maini