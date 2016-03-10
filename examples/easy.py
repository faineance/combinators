from stateless import stateless


def inc(state):
    return state + 1


def dec(state):
    return state - 1


def actions():
    while True:
        cmd = input('> ')
        if cmd in ['+', '-']:
            yield cmd
        else:
            raise StopIteration

res = stateless(0, actions(), {'+': inc, '-': dec})

print(res)
