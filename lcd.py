import re
import sys

# Define the dictionary with all the number possible, 3 lines by number to easily join them after
dict_num = {
    '0': {
        'line1': ' _ ',
        'line2': '| |',
        'line3': '|_|'
    },
    '1': {
        'line1': '   ',
        'line2': '  |',
        'line3': '  |'
    },
    '2': {
        'line1': ' _ ',
        'line2': ' _|',
        'line3': '|_ '
    },
    '3': {
        'line1': ' _ ',
        'line2': ' _|',
        'line3': ' _|'
    },
    '4': {
        'line1': '   ',
        'line2': '|_|',
        'line3': '  |'
    },
    '5': {
        'line1': ' _ ',
        'line2': '|_ ',
        'line3': ' _|'
    },
    '6': {
        'line1': ' _ ',
        'line2': '|_ ',
        'line3': '|_|'
    },
    '7': {
        'line1': ' _ ',
        'line2': '  |',
        'line3': '  |'
    },
    '8': {
        'line1': ' _ ',
        'line2': '|_|',
        'line3': '|_|'
    },
    '9': {
        'line1': ' _ ',
        'line2': '|_|',
        'line3': '  |'
    }
}

def print_num_lcd(num, test=False):
    # num = 28575079
    # Convert num in to a string
    if type(num) != str:
        str_num = str(num)
    else:
        str_num = num
    # Remove non number from the string (just in case)
    str_num = re.sub('[^0-9]','', str_num)
    # Extract digit from number
    split_num = [num for num in str_num]

    # Define the 3 lines of the lcd screen
    line1, line2, line3 = str(), str(), str()
    # Iterate to build the 3 lines of the LCD
    for (i, num) in enumerate(split_num, 1):
        line1 += dict_num[num]['line1']
        line2 += dict_num[num]['line2']
        line3 += dict_num[num]['line3']
        if i != len(split_num):
            # Add space between number if not the last number
            line1 += ' '
            line2 += ' '
            line3 += ' '
    # Join the 3 lines before printing
    final_str = '\n'.join([line1, line2, line3])
    if test:
        return final_str
    else:
        print(final_str)

# We do some test 
# num = 123456789
# res = """\
#      _   _       _   _   _   _   _ 
#   |  _|  _| |_| |_  |_    | |_| |_|
#   | |_   _|   |  _| |_|   | |_|   |\
# """
# assert res == print_num_lcd(num, True)
# num = 28575079
# res = """\
#  _   _   _   _   _   _   _   _ 
#  _| |_| |_    | |_  | |   | |_|
# |_  |_|  _|   |  _| |_|   |   |\
# """
# assert res == print_num_lcd(num, True)

# num = 2873440985671
# res = """\
#  _   _   _   _           _   _   _   _   _   _     
#  _| |_|   |  _| |_| |_| | | |_| |_| |_  |_    |   |
# |_  |_|   |  _|   |   | |_|   | |_|  _| |_|   |   |\
# """
# assert res == print_num_lcd(num, True)
# num = '12790yutyn%^&*3456'
# res = """\
#      _   _   _   _   _       _   _ 
#   |  _|   | |_| | |  _| |_| |_  |_ 
#   | |_    |   | |_|  _|   |  _| |_|\
# """
# assert res == print_num_lcd(num, True)

if len(sys.argv) < 2:
    print('Not enough argument')
elif len(sys.argv) > 2:
    print('Too many arguements')
elif len(sys.argv) == 2:
    print_num_lcd(sys.argv[1])
    