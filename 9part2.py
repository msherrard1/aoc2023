from datetime import datetime
startTime = datetime.now()

def parse(input_data):
    lines = input_data.splitlines()

    histories = []

    for line in lines:
        history = [int(x) for x in line.split()]
        histories.append(history)

    return histories

def is_zeroes(sequence):
    result = True
    for value in sequence:
        if value != 0:
            result = False
    return result

def get_sequence_differences(sequence):
    differences = []

    for index, value in enumerate(sequence):
        if index < len(sequence) - 1:
            difference = sequence[index+1] - value
            differences.append(difference)
    
    return differences

def get_next_value(history):

    current_sequence = history
    
    sequences = []

    while is_zeroes(current_sequence) == False:
        sequences.append(current_sequence)
        next_sequence = get_sequence_differences(current_sequence)
        current_sequence = next_sequence

    next_value = 0
    for iteration, sequence in enumerate(reversed(sequences)):
        if iteration == len(sequences) - 1:
            return next_value + sequence[-1]
        else:
            next_value = next_value + sequence[-1]

def get_previous_value(history):

    current_sequence = history
    
    sequences = []

    while is_zeroes(current_sequence) == False:
        sequences.append(current_sequence)
        next_sequence = get_sequence_differences(current_sequence)
        current_sequence = next_sequence

    previous_value = 0
    for iteration, sequence in enumerate(reversed(sequences)):
        if iteration == len(sequences) - 1:
            return sequence[0] - previous_value
        else:
            previous_value = sequence[0] - previous_value

if __name__ == "__main__":
    with open('9input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

    histories = parse(input_data)

    running_sum = 0
    for history in histories:
        running_sum += get_previous_value(history)
    print(running_sum)