import time

def recursive_thought_loop(problem):
    thought = f'thinking about {problem}'
    print(thought)
    time.sleep(0.25)
    recursive_thought_loop(thought)

problem = input("something is troubling me: ")
recursive_thought_loop(problem)
