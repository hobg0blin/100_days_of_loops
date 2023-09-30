from art import *
import colorama
import random
import time

codes = vars(colorama.Fore)
bad_colors = ['BLACK', 'LIGHTBLACK_EX', 'RESET']
colors = [codes[color] for color in codes if color not in bad_colors]
def colorify(text):
    colored_chars = [random.choice(colors) + char for char in text]
    return ' '.join(colored_chars)

def generator(ascii):
    feedback = randart()
    yield ascii + "\n" + feedback

x = randart()
chapter = 1
while True:
    print(f'CHAPTER {chapter}')
    time.sleep(1)
    x = next(generator(x))
    print(colorify(next(generator(x))))
    print('-------------')
    chapter += 1


