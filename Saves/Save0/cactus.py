from move_to import move_to

move_to(0, 0)
ws = get_world_size()


def reset():
    clear()

def harvesting_routine():
    i = 0
    while True:
        if measure() != 9:
            harvest()
        if get_ground_type() == Grounds.Grassland:
            till()
        else :
            pass
        plant(Entities.Cactus)
        if measure() != 9 :
            harvest()
            plant(Entities.Cactus)
            use_item(Items.Water)
            continue
        move(North)

        if get_pos_y() == 0 :
            break


while True:
    for _ in range(max_drones()):
        if spawn_drone(harvesting_routine):
            move(East)

    harvesting_routine()

    while num_drones() > 1:
        do_a_flip()

    if can_harvest():
        harvest()
        move_to(0, 0)
