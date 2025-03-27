'''
# First attempt, basic with a focus on simplicity and functionality
hardcoded_dungeon = [
    [1,1,1,1,1],
    [1,0,2,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

the_dungeon = ""

for each_row in hardcoded_dungeon:
    for each_column in each_row:
        match each_column:
            case 0:
                the_dungeon += " "
            case 1:
                the_dungeon += "#"
            case 2:
                the_dungeon += "@"
    the_dungeon += "\n"

print(the_dungeon)
'''

# Second attempt, refactoring
Empty = 0
Wall = 1
Character = 2

dungeon_sprite_map = {
    Empty: ' ',
    Wall: '#',
    Character: '@'
}

hardcoded_dungeon = [
    [Wall, Wall,  Wall,      Wall,  Wall],
    [Wall, Empty, Character, Empty, Wall],
    [Wall, Empty, Empty,     Empty, Wall],
    [Wall, Wall,  Wall,      Wall,  Wall]
]

def render_dungeon(dungeon):
    """Convert a dungeon to a string representation"""
    dungeon_str = ""
    for each_row in dungeon:
        for each_column in each_row:
            dungeon_str += dungeon_sprite_map[each_column]
        dungeon_str += "\n"
    return dungeon_str

def render_dungeon_optimised(dungeon):
    """Convert a dungeon to a string representation. Use join() instead of for loops with lots of string concatenations"""
    return "\n".join("".join(dungeon_sprite_map[cell] for cell in row) for row in dungeon)

print("Dungeon rendered using for loops and string concatenation: ")
print(render_dungeon(hardcoded_dungeon))

print("Dungeon rendered using join() method: ")
print(render_dungeon_optimised(hardcoded_dungeon))

print()
#####
# Curiosity test for performance of the two methods
import timeit
num_iterations = 1000

# Generate a large dungeon to test with
large_dungeon = [[1 if x == 0 or x == 49 or y == 0 or y == 49 else 0 for x in range(50)] for y in range(50)]

print("Large Dungeon: ")
print(render_dungeon_optimised(large_dungeon))

for_loop_time = timeit.timeit(lambda: render_dungeon(large_dungeon), number=num_iterations)
join_method_time = timeit.timeit(lambda: render_dungeon_optimised(large_dungeon), number=num_iterations)

print(f"For loop time: {for_loop_time:.6f} seconds for {num_iterations} iterations.")
print(f"join() method  time: {join_method_time:.6f} seconds for {num_iterations} iterations.")

speedup = for_loop_time / join_method_time if join_method_time > 0 else float('inf')
print(f"join() method is {speedup:.2f}x faster")
