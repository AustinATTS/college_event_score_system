events = []
def add_event(event, type, participant, score):
    events.append(f"{event} - {type} - {participant}, {score}")

def return_events():
    return events

def clear_events():
    events.clear()
