import math
from collections import defaultdict
from functools import cmp_to_key


SECOND = 1
MINUTE = 60*SECOND
HOUR = 60*MINUTE


def get_seconds_number(time_str):
    """
    For the time string in format hh:mm:ss return total number of seconds.
    """
    hours, minutes, seconds = time_str.split(':')
    return int(hours)*HOUR + int(minutes)*MINUTE + int(seconds)*SECOND


def parse_line(line):
    """
    Return (seconds,cents) tuple for a given call record
    """
    time_part, _, num_part = line.partition(',')
    duration_seconds = get_seconds_number(time_part)
    cost_for_call = calculate_call_cost(duration_seconds)
    return duration_seconds, cost_for_call, num_part.strip()


def calculate_call_cost(duration_seconds):
    if duration_seconds < 5*MINUTE:
        return duration_seconds*3
    else:
        total_started_minutes = math.ceil(duration_seconds/MINUTE)
        return total_started_minutes*150


def calculate_total_price(costs, durations):
    def cmp(item1, item2):
        num1, dur1 = item1
        num2, dur2 = item2
        if dur1 == dur2:
            if num1 == num2:
                return 0
            elif num1 < num2:
                return 1
            else:
                return -1
        elif dur1 > dur2:
            return 1
        else:
            return -1

    longest_duration_number = max(durations.items(), key=cmp_to_key(cmp))[0]
    # Remove phone number with longest calls duration from total expenses
    costs.pop(longest_duration_number)
    return sum(costs.values())


def main():
    costs = defaultdict(int)
    durations = defaultdict(int)
    import pdb; pdb.set_trace()
    with open('input.txt') as f:
        for line in f:
            duration, cost, number = parse_line(line)
            costs[number] += cost
            durations[number] += duration

    print(calculate_total_price(costs, durations))

if __name__ == '__main__':
    main()
