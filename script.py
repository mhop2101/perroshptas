from datetime import datetime
import time
import json

current_week_day = datetime.today().weekday()

week_days_map = {
    0: 'l',
    1: 'm',
    2: 'i',
    3: 'j',
    4: 'v',
    5: 's',
    6: 'd',
}

current_week_day_key = week_days_map[current_week_day]


def get_available_room(room_code, info) -> list:
    rooms_list = []

    for element in info:
        for schedule in element['schedules']:
            rooms_list.append(schedule['classroom'])

    unique_rooms = list(set(rooms_list))

    rooms_schedules = {}

    for class_info in info:
        for schedule in class_info['schedules']:
            if schedule['classroom'] in rooms_schedules.keys():
                rooms_schedules[schedule['classroom']].append(schedule)
            else:
                rooms_schedules[schedule['classroom']] = [schedule]

    available_rooms = unique_rooms.copy()

    for room in rooms_schedules:
        for schedule in rooms_schedules[room]:
            if schedule[current_week_day_key] is None:
                continue
            else:
                start_time = schedule['time_ini']
                end_time = schedule['time_fin']
                current_time = time.strftime("%H%M")
                if check_time_in_range(start_time, end_time, current_time):
                    try:
                        available_rooms.remove(room)
                    except:
                        pass
    in_building = []

    for room in available_rooms:
        if room[0:3] == room_code:
            in_building.append(room)

    return in_building


def check_time_in_range(start_time: str, end_time: str, current_time: str) -> bool:
    start_time = datetime.strptime(start_time, '%H%M')
    end_time = datetime.strptime(end_time, '%H%M')
    current_time = datetime.strptime(current_time, '%H%M')

    if start_time <= current_time and current_time <= end_time:
        return True
    return False
