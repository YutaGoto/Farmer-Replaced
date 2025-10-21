clear()

ws = get_world_size()

def harvest_sunflowers():
    while True:
        if can_harvest():
            harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        plant(Entities.Sunflower)
        if get_water() < 0.5:
            use_item(Items.Water)
        move(North)
    
while True:
    for _ in range(max_drones()):
        if spawn_drone(harvest_sunflowers):
            move(East)

    harvest_sunflowers()
    