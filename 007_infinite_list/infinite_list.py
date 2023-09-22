import time
finite_list = []

def become_infinite(next_layer):
    next_layer.append([])
    print(finite_list)

    time.sleep(0.01)
    print(
        '---- becoming infinite ----'
    )
    become_infinite(next_layer[0])

become_infinite(finite_list)
