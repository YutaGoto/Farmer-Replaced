from move_to import move_to

def init():
    clear()
    # change_hat(Hats.Dinosaur_Hat)
    ws = get_world_size()
    # ninjin
    for i in range(4):
        for _ in range(ws):
            if can_harvest():
                harvest()
            till()
            plant(Entities.Carrot)
            move(East)

        move_to(0, get_pos_y())
        move(North)

    move_to(0, 20)


    # himawari
    for i in range(ws):
        if can_harvest():
            harvest()
        till()
        plant(Entities.Sunflower)
        move(East)

    move_to(0, 21)
    for i in range(ws):
        if can_harvest():
            harvest()
        till()
        plant(Entities.Sunflower)
        move(East)

    move_to(0, 4)

    # kabocha
    for i in range(8):
        for j in range(8):
            if can_harvest():
                harvest()
            till()
            plant(Entities.Pumpkin)
            if get_pos_y() == 11:
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
            else:
                move(North)

        move(East)

    move_to(8, 8)

    # saboten
    for i in range(8):
        for j in range(8):
            if can_harvest():
                harvest()
            till()
            plant(Entities.Cactus)
            if get_pos_y() == 15:
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
                move(South)
            else:
                move(North)
        move(East)

    move_to(0, 0)
    