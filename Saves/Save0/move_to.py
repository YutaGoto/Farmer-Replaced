def move_to(x, y):

    while True:
        current_x = get_pos_x()

        if current_x == x:
            break

        if current_x > x:
            move(West)
        else:
            move(East)

    while True:
        current_y = get_pos_y()

        if current_y == y:
            break

        if current_y > y:
            move(South)
        else:
            move(North)
            