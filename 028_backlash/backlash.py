prev_node = "node_0"
def backlash(phrase, limit, prev_node):
    print(f'node_{limit}[label="Criticizing the \\n' + phrase + '"];')
    print(f"{prev_node}->node_{limit};")
    prev_node = "node_" + str(limit)
    if (limit > 0):
        phrase = "criticism of the \\n" + phrase

        backlash(phrase, limit-1, prev_node)
    else:
        return

backlash('thing', 20, prev_node)
