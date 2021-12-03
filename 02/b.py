pos, depth, aim = 0, 0, 0

with open('input.txt') as f:
    for line in f.readlines():
        cmd, val = line.split()
        val = int(val)

        if cmd == 'down':
            aim += val
        elif cmd == 'up': 
            aim -= val
        elif cmd == 'forward':
            pos += val
            depth += aim * val

print(pos * depth)