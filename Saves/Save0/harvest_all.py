from move_to import move_to

def harvest_column():
    for _ in range(get_world_size()):
        if can_harvest():
        harvest()   
        move(North)

move_to(0, 0)

while True:
    if spawn_drone(harvest_column):
        move(East)
