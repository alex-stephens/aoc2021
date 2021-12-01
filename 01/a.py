prev = None
count = 0
with open('input.txt') as f:
    for line in f.readlines():
        x = int(line)
        if prev is not None and x > prev:
            count += 1
        prev = x

print(count)