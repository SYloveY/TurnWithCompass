def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45
    face_dir = directions.index(facing)
    turn_dir = (face_dir + turns) % len(directions)
    return directions[turn_dir]


print(direction('S', 180))
