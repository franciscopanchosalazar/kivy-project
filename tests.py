
counter_a = 0
counter_b = 0

if counter_a == 45:
    counter_a = 40

if counter_b == 45:
    counter_b = 40

#if counter_a >= 40 and counter_b >=40:


def add_points_a():
    global counter_a
    counter_a += 15


def sub_points_a():
    global counter_a
    counter_a -= 15


def add_points_b():
    global counter_b
    counter_b += 15


def sub_points_b():
    global counter_b
    counter_b -= 15


def reset_counters():
    global counter_a, counter_b
    counter_a = 0
    counter_b = 0

