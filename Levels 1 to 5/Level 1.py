
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


