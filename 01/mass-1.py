# part 1

f = open('input.txt', 'r')
mass = 0

for line in f:
    m = int(line)
    m = (m//3) - 2
    mass += m

print(mass)
