clear()

def solve_maze_1():
    plant(Entities.Bush)
    substance = 1 * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    while True:
        if can_harvest():
            harvest()
            plant(Entities.Bush)
            use_item(Items.Weird_Substance, substance)

while True:
    for _ in range(max_drones()):
        if spawn_drone(solve_maze_1):
            move(East)
    solve_maze_1()

    