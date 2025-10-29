next_x = -1
next_y = -1
clear()
# set_world_size(6)
change_hat(Hats.Dinosaur_Hat)
ws = get_world_size()
flag = False

def move_snake():
    global flag
    if flag:
        if move(West):
            pass
        elif move(South):
            pass

        if get_pos_y() == 0 and get_pos_x() == 0:
            flag = False
    elif get_pos_y() % 2 == 0:
        if move(East):
            pass
        else:
            if move(North):
                pass
            else:
                change_hat(Hats.Brown_Hat)
                change_hat(Hats.Dinosaur_Hat)

    else:
        if get_pos_y() == ws - 1:
            flag = True
            if move(West):
                pass
            elif move(South):
                pass
            else:
                change_hat(Hats.Brown_Hat)
                change_hat(Hats.Dinosaur_Hat)


        elif get_pos_x() == 1:
            if move(North):
                pass
            else:
                change_hat(Hats.Brown_Hat)
                change_hat(Hats.Dinosaur_Hat)
        else:
            if move(West):
                pass
            else:
                if move(North):
                    pass
                else:
                    change_hat(Hats.Brown_Hat)
                    change_hat(Hats.Dinosaur_Hat)

while True:
    if measure() != None:
        quick_print(measure())
        quick_print(get_pos_x())
        quick_print(get_pos_y())
        next_x,next_y  = measure()

    if next_x == get_pos_x():
        if next_y > get_pos_y():
            if move(North):
                continue
            else:
                change_hat(Hats.Brown_Hat)
                change_hat(Hats.Dinosaur_Hat)
                next_x,next_y  = measure()
        elif next_y < get_pos_y():
            move_snake()
        else:
            change_hat(Hats.Brown_Hat)
            change_hat(Hats.Dinosaur_Hat)
            next_x,next_y  = measure()

    else:
        move_snake()
        