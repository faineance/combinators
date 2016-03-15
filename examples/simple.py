from combinators import stateless


def actions():
    while True:
        cmd = input('> ')
        if cmd in ['+', '-']:

            yield cmd
        else:
            raise StopIteration


res = stateless(0, actions(), {'+': lambda x: x + 1, '-': lambda x: x - 1})

print(res)
