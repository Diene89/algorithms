def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    students = 0

    for start_time, end_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        elif start_time <= target_time <= end_time:
            students += 1
    return students
