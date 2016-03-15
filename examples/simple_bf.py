from combinators import stateless


def inc(state):
    state['tape'][state['sp']] += 1
    return state


def dec(state):
    state['tape'][state['sp']] -= 1
    return state


def next(state):
    state['sp'] += 1
    return state


def prev(state):
    state['sp'] -= 1
    return state


def write(state):
    print(state['tape'][state['sp']])
    return state


def read(state):
    state['tape'][state['sp']] = int(input())
    return state


def actions():
    while True:
        cmds = list(filter(lambda x: x in ['.', ',', '<', '>', '+', '-'], input('~ ')))
        if cmds:
            for cmd in cmds:
                yield cmd
        else:
            raise StopIteration


initial_state = {"sp": 10, "tape": [0] * 20}

dispatch = {
    '+': inc,
    '-': dec,
    '>': next,
    '<': prev,
    '.': write,
    ',': read,
}

res = stateless(initial_state, actions(), dispatch)

print(res)
