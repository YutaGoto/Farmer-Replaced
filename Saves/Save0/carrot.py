from move_to import move_to

move_to(0, 0)
ws = get_world_size()
move_arr = [East, West]

def harvest_carrot():
    c = 0
    while True:
        if can_harvest():
            harvest()
        else:
            if get_entity_type() == None:
                plant(Entities.Carrot)
            move(move_arr[random() * len(move_arr) // 1])
            
        if get_ground_type() != Grounds.Soil:
            till()

        if get_entity_type() == None:
            if c % ws == 1 or c % ws == (ws - 2):
                plant(Entities.Sunflower)
            else:
                plant(Entities.Carrot)
 
        if get_water() < 0.5:
            use_item(Items.Water)
            
        move(North)
        c += 1
        if c % ws == 0:
            c = 0
            move(East)
    
while True:
    for _ in range(max_drones()):
        if spawn_drone(harvest_carrot):
            move(East)
            move(East)
    harvest_carrot()
    