# part 2

src = [int(s) for s in open('input.txt', 'r').readline().split(',')]

noun = 0
verb = 0
found = False
while not found:
    prog = src.copy()
    prog[1] = noun
    prog[2] = verb

    p = 0
    while True:
        op = prog[p]
        if op == 99:
            break

        val1, val2, wPos = prog[p+1], prog[p+2], prog[p+3]
        if op == 1: # add
            prog[wPos] = prog[val1] + prog[val2]
        elif op == 2: # multiply
            prog[wPos] = prog[val1] * prog[val2]
        else:
            raise ValueError('Encountered invalid opcode')
        p += 4

    if prog[0] == 19690720:
        found = True
    else:
        # print("noun: %d, verb: %d, result: %d" % (noun, verb, prog[0]))
        verb += 1
        if verb == 100:
            verb = 0
            noun += 1

print("noun: %d, verb: %d, answer: %d" % (noun, verb, 100 * noun + verb))
