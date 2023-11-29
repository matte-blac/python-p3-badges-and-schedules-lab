def badge_maker(name):
    badge_message = f'Hello, my name is {name}.'
    return badge_message

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(badge_maker(name))
    return badge_messages

def assign_rooms(names):
    room_assignments = []
    current_room = 1
    for name in names:
        room_assignment = f"Hello, {name}! You'll be assigned to room {current_room}!"
        room_assignments.append(room_assignment)
        current_room += 1
    return room_assignments

def printer(names):
    badge_messages = batch_badge_creator(names)
    for badge_message in badge_messages:
        print(badge_message)

    room_assignments = assign_rooms(names)
    for room_assignment in room_assignments:
        print(room_assignment)

# printer['Arel', 'Carol']