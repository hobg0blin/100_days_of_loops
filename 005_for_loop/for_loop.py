import nltk
from pyfiglet import Figlet
import time
import string
# nltk.download('gutenberg')
# nltk.download('punkt')
# nltk.download('stopwords')
stop = set(nltk.corpus.stopwords.words('english'))

moby_dick = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
print('moby dick: ', moby_dick)
f = Figlet(font='slant')
for idx, word in enumerate(moby_dick):
    #print(f"{idx} {word}")
    if word == "Ishmael":
        break

for word in moby_dick[4707:]:
    if word not in string.punctuation:
        print(f.renderText(word))
        time.sleep(0.5)
