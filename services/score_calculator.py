points = [10, 8, 6, 4, 2]


def multiple_calculate_score(event_one, event_two, event_three, event_four, event_five):
    total_score = points[event_one - 1] + points[event_two - 1] + points[event_three - 1] + points[event_four - 1] + points[event_five - 1]
    return total_score


def solo_calculate_score(event_one):
    total_score = points[event_one - 1]
    return total_score

display_points = [20, 40, 60, 80, 100]

def multiple_display_score(event_one, event_two, event_three, event_four, event_five):
    display_score = display_points[event_one - 1] + display_points[event_two - 1] + display_points[event_three - 1] + display_points[event_four - 1] + display_points[event_five - 1]
    return display_score

def solo_display_score(event_one):
    display_score = display_points[event_one - 1]
    return display_score
