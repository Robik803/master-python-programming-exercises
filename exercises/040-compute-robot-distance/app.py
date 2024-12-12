import math

def compute_robot_distance(movement_seq):
    pos = [0,0]
    for move in movement_seq:
        direction,distance = move.split(' ')
        if direction == "UP":
            pos[0] += int(distance)
        elif direction == "DOWN":
            pos[0] -= int(distance)
        elif direction == "LEFT":
            pos[1] += int(distance)
        elif direction == "RIGHT":
            pos[1] -= int(distance)
    return round(math.sqrt(pos[0]**2+pos[1]**2))