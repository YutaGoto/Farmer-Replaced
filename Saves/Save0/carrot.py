clear()

ws = get_world_size()

while True:
    for i in range(ws):
        for j in range(ws):
            if can_harvest():
                harvest()

            if get_ground_type() != Grounds.Soil:
                till()

            if i == 21:
                plant(Entities.Sunflower)
            else:
                plant(Entities.Carrot)

            move(North)
        move(East)
        