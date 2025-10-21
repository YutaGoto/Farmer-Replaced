from move_to import move_to

ws = get_world_size()

def harvesting_routine():
    unharvestable_p = []
    init_flag = True
    i = 0

    while True:
        while init_flag:
            if get_ground_type() == Grounds.Grassland:
                harvest()
                till()

            if not can_harvest():
                unharvestable_p.append((get_pos_x(), get_pos_y()))
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)

            move(North)

            if get_pos_y() == 0:
                init_flag = False

        while len(unharvestable_p) > 0:
            for pos in unharvestable_p:
                move_to(pos[0], pos[1])
                if can_harvest() and get_entity_type() == Entities.Pumpkin:
                    unharvestable_p.remove(pos)
                    break
                else:
                    plant(Entities.Pumpkin)

        break

while True:
    move_to(0, 0)
    for _ in range(max_drones()):
        if spawn_drone(harvesting_routine):
            move(East)

    harvesting_routine()

    while True:
        move_to(ws - 1, ws - 1)
        if can_harvest() and num_drones() == 1:
            harvest()
            break
