import random
class Ouroboros():
    def mouth(self):
        self.tail()
    def tail(self):
        self.mouth()

snek = Ouroboros()
start = random.random()
if start > 0.5:
    snek.mouth()
else:
    snek.tail()