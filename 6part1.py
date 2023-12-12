def parse(input_data):
    lines = input_data.splitlines()

    times = lines[0].split()
    distances = lines[1].split()

    races = {}

    for race_no in range(1, len(times)):
        time = int(times[race_no])
        distance = int(distances[race_no])
        races[race_no] = [ time, distance ]

    return races;

def get_number_winning_options(race_time, record_distance):
    
    winning_options = []

    for press_time in range(1, race_time):
        travel_time = race_time - press_time
        if travel_time*press_time > record_distance:
            winning_options.append(press_time)

    return len(winning_options)

if __name__ == "__main__":
    with open('6input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """Time:      7  15   30
# Distance:  9  40  200"""

    races = parse(input_data)

    running_product = 1

    for race_no, (time, distance) in races.items():
        running_product *= get_number_winning_options(time, distance)
    
    print(running_product)
    