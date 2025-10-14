clear()

ws = get_world_size()

while True:
    for i in range(ws):
        for j in range(ws):
            if can_harvest():
                harvest()

            if i == 21:
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Sunflower)
            elif i % 2 == 0 and j % 2 == 1 or i % 2 == 1 and j % 2 == 0:
                plant(Entities.Tree)

            move(North)
        move(East)
        