import init

init.init()
ws = get_world_size()

while True:
    for j in range(ws):
        for i in range(ws):
            if can_harvest():
                harvest()

            if i <= 3:
                plant(Entities.Carrot)
            elif i == 2 and j % 2 == 1:
                plant(Entities.Carrot)
            elif (i == 17 or i == 19) and j % 2 == 0 or (i == 13 or i == 15) and j % 2 == 0 and j < 8:
                plant(Entities.Tree)
                use_item(Items.Water)
            elif i == 20 or i == 21:
                plant(Entities.Sunflower)
                use_item(Items.Water)
            elif i >= 4 and i < 12 and j <= 7:
                plant(Entities.Pumpkin)
                # use_item(Items.Fertilizer)
                use_item(Items.Water)
            elif i >= 8 and j >= 8 and i < 16 and j < 16:
                use_item(Items.Water)
                plant(Entities.Cactus)

            move(North)
        move(East)
