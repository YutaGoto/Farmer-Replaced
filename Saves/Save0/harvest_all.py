ws = get_world_size()
c = 0

while c < ws ** 2:
    for i in range(ws):
        for j in range(ws):
            if can_harvest():
                harvest()
            c += 1
            move(North)
        move(East)