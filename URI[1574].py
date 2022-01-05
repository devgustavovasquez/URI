qtd = int(input())


def process_instructs(actually_instructs, position=0):
    counter = 0
    for instruct in actually_instructs:
        if instruct == 'LEFT':
            position -= 1
        elif instruct == 'RIGHT':
            position += 1
        else:
            same_instruct = int(instruct[8:]) - 1
            if actually_instructs[same_instruct] == 'LEFT':
                position -= 1
                actually_instructs[counter] = 'LEFT'
            else:
                position += 1
                actually_instructs[counter] = 'RIGHT'
        counter += 1
    print(position)
    return None


def get_instructs():
    instructs = []
    for i in range(qtd):
        qtd_instructs = int(input())
        for n in range(qtd_instructs):
            instructs.append(input())
        process_instructs(instructs)
        instructs = []
    return None


get_instructs()
