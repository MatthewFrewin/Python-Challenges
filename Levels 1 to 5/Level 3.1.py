# 3.1 Random Dungeon Generator
import random
from copy import deepcopy

Empty = 0
Wall = 1
Character = 2

class RandomDungeonGenerator:
    def completely_random(self, width, height, seed=0):
        if seed > 0:
            random.seed(seed)

        return [[random.randint(0,1)for _ in range(width)] for _ in range(height)]

    # Bonus task using cellular automaton
    def cellular_automaton_processor(self, noise_grid, number_iterations):
        # Note: Check the following YouTube video to get an intro to cellular automaton: https://www.youtube.com/watch?v=slTEz6555Ts
        grid_height, grid_width = len(noise_grid), len(noise_grid[0])

        for i in range(number_iterations):
            temp_grid = deepcopy(noise_grid)

            for y in range(grid_height):
                for x in range(grid_width):
                    # Count the number of wall tiles in the neighbourhood of the current tile (Moore Neighborhood)
                    wall_count = 0
                    moore_range = [-1,0,1]
                    for j in moore_range:
                        for k in moore_range:
                            if(j == 0 and k == 0):      # Skip the centre tile
                                continue
                            nx, ny = x + k, y + j

                            if 0 <= ny < grid_height and 0 <= nx < grid_width:
                                # Check if the tile is a Wall
                                if temp_grid[ny][nx] == Wall:
                                    wall_count += 1
                            else:
                                wall_count += 1

                    noise_grid[y][x] = Wall if wall_count > 4 else Empty

        return noise_grid

    def generate_empty_grid(self, width, height, create_outer_walls):
        if create_outer_walls:
            return [
                [Wall if x == 0 or x == width - 1 or y == 0 or y == height - 1 else Empty for x in range(width)]
                for y in range(height)]
        else:
            return [[Empty for x in range(width)] for y in range(height)]

    def render(self, dungeon):
        """Convert a dungeon to a string representation"""
        dungeon_sprite_map = {Empty: ".", Wall: "#"}
        return "\n".join("".join(dungeon_sprite_map[cell] for cell in row) for row in dungeon)


dungeon_generator = RandomDungeonGenerator()
random_dungeon = dungeon_generator.completely_random(150, 150, 222)
rendered_random_dungeon = dungeon_generator.render(random_dungeon)

cellular_automaton_dungeon = dungeon_generator.cellular_automaton_processor(random_dungeon, 3)

print(rendered_random_dungeon)
print()
print(dungeon_generator.render(cellular_automaton_dungeon))
