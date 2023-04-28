

def generate_payload(context, room_x, room_y, start_x, start_y, dirt_positions, instructions):
    context.dirt_positions = get_dirt_list(dirt_positions)

    payload = {
        "roomSize": [int(room_x), int(room_y)],
        "coords": [int(start_x), int(start_y)],
        "patches": context.dirt_positions,
        "instructions": instructions
    }

    return payload


def generate_instructions_payload(context, instructions):
    payload = {
        "roomSize": [context.room_x, context.room_y],
        "coords": [context.start_x, context.start_y],
        "patches": context.dirt_positions,
        "instructions": instructions
    }

    return payload




def get_dirt_list(dirt_positions):
    dirt_list = []
    #context.dirt_positions = []
    for position in dirt_positions.split(';'):
        x, y = position.split(',')
        #context.dirt_positions.append((int(x), int(y)))
        dirt_list.append((int(x), int(y)))
    return dirt_list


def generate_incomplete_payload(room_x, room_y, start_x, start_y, instructions):
    payload = {
        "roomSize": [int(room_x), int(room_y)],
        "coords": [int(start_x), int(start_y)],
        "instructions": instructions
    }

    return payload


