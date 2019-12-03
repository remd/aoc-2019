# part 2

f = open('input.txt', 'r')
mass = 0

def fReq(m):
    fuel = (m//3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fReq(fuel)

for line in f:
    m = int(line)
    mass += fReq(m)

print(mass)
