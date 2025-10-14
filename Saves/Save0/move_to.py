def move_to(x, y):
    while True:
        if get_pos_x() == x:
            break
        
        move(East)
    
    while True:
        if get_pos_y() == y:
            break
        
        move(North)
    