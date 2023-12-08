import csv
import re

garbled_inputs = []

numeral_string_to_digit = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four": "4",
        "five": "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

# def replace_digit_names_with_numerals(str_to_replace, position = 0):
#     if position == len(str_to_replace):
#         return str_to_replace

#     str_before_search = str_to_replace[:position]
#     str_to_search = str_to_replace[position:]

#     for numeral_string, numeral_digit in numeral_string_to_digit.items():
#         if str_to_search.startswith(numeral_string):
#             str_to_search = str_to_search.replace(numeral_string,numeral_digit,1)
    
#     new_string = str_before_search + str_to_search

#     return replace_digit_names_with_numerals(new_string,position=position+1)

# # def get_number_from_garbled(garbled):
# #     firstDigit = None
# #     lastDigit = None

# #     garbled = replace_digit_names_with_numerals(garbled)

# #     for character in garbled:
# #         if character.isdigit():
# #             if firstDigit == None:
# #                 firstDigit = character
# #             lastDigit = character
    
# #     return int(firstDigit + lastDigit)

def get_digit_as_character(number):
    if number in numeral_string_to_digit.keys():
        return numeral_string_to_digit[number]
    else:
        return number

def get_number_from_garbled(garbled):
    firstDigit = None
    lastDigit = None

    numbers = ['0','1','2','3','4','5','6','7','8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    matches = {}

    for pos in range(len(garbled)):
        for number in numbers:
            if garbled[pos:].startswith(number):
                matches.update({ pos : number })
    
    first_match_pos = min(matches.keys())
    last_match_pos = max(matches.keys())

    first_digit = get_digit_as_character(matches[first_match_pos])
    last_digit = get_digit_as_character(matches[last_match_pos])

    return int(first_digit + last_digit)

with open('1input.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    garbled_inputs.append(row[0])

ungarbled_values = []

for garbled_input in garbled_inputs:
    ungarbled = get_number_from_garbled(garbled_input)
    ungarbled_values.append(ungarbled)

print(sum(ungarbled_values))

#test_strings = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
# test_strings = ['fiveqtvbrzlqtlnflvtnqpjlrtwo9eightfourqlstm']

#for test_string in test_strings:
#    print(get_number_from_garbled(test_string))