# part 1

prog = [int(s) for s in  open('input.txt', 'r').readline().split(',')]
print(prog)

prog[1] = 12
prog[2] = 2
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

print(prog)
