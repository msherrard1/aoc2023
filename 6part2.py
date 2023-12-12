from datetime import datetime
startTime = datetime.now()

def parse(input_data):
    lines = input_data.splitlines()

    time_digits = lines[0].split()[1:]
    distance_digits = lines[1].split()[1:]

    time = int(''.join(time_digits))
    distance = int(''.join(distance_digits))

    return (time, distance)

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

    race = parse(input_data)
    print(get_number_winning_options(race[0],race[1]))

    # running_product = 1

    # for race_no, (time, distance) in races.items():
    #     running_product *= get_number_winning_options(time, distance)
    
    # print(running_product)
    
    print(datetime.now() - startTime)