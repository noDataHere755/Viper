import main

gen = main.strt()

try:
    msg = next(gen)
    
    # start generator
    while True:
        msg=str(msg)
        if msg.endswith(':'):
            a = input(msg + ' ')
            msg = gen.send(a)
        elif msg.endswith('>'):
            a = input(msg + ' ')
            msg = gen.send(a)
        elif msg=="None":
            msg=next(gen)
        else:
            print(msg)
            msg = next(gen)
except StopIteration:
    pass
