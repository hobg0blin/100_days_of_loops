import nltk
import markovify
import string
import time

import colorama
import random

codes = vars(colorama.Fore)
bad_colors = ['BLACK', 'LIGHTBLACK_EX', 'RESET']
colors = [codes[color] for color in codes if color not in bad_colors]
def colorify(text):
    colored_chars = [random.choice(colors) + char for char in text]
    return ' '.join(colored_chars)

# nltk.download('gutenberg')
moby_dick = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
model = markovify.Text(moby_dick)

def generator(start_text, iters):
    num = 0
    last = start_text
    while num < iters:
        start_word = last.split(" ")
        feedback = last_word(start_word, -1)
        last = feedback
        yield  feedback.capitalize()
        num +=1

def last_word(start_word_list, index):
    try:
        return model.make_sentence_with_start(start_word_list[index].translate(str.maketrans('', '', string.punctuation)), False)
    except:
        return last_word(start_word_list, index-1)


x = model.make_sentence()
iterator = 100
chapter = 1
book = generator(x, iterator)
while iterator > 0:
    output = colorify(next(book).split(" "))
    if (iterator and iterator % 5 == 0):
        print('---------------------------')
        print(f'CHAPTER {chapter}')
        print(output)
        chapter +=1
    else:
        print(output)
    time.sleep(1)
    iterator-=1


