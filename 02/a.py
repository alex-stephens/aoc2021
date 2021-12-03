pos, depth = 0, 0
cmd = {'forward': (1,0), 'up': (0,-1), 'down': (0,1)}

with open('input.txt') as f:
    for line in f.readlines():
        c, val = line.split()
        val = int(val)

        pos += cmd[c][0] * val
        depth += cmd[c][1] * val

print(pos * depth)