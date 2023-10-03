import time
import colorama
import random
first = "August "
last = " Luhrs"
codes = vars(colorama.Fore)
bad_colors = ['BLACK', 'LIGHTBLACK_EX', 'RESET']
colors = [codes[color] for color in codes if color not in bad_colors]
def colorify(text):
    colored_text = random.choice(colors) + text
    return colored_text


def infinite_name(first, last):
    print(colorify(first)+ colorify(last))
    time.sleep(1)
    infinite_name(first + first, last + last)

infinite_name(first, last)
