nums = []
with open('input.txt') as f:
    for line in f.readlines():
        nums.append(int(line))

count = 0
w = 3 # window length
for i in range(w, len(nums)):
    if sum(nums[i-w+1:i+1]) > sum(nums[i-w:i]):
        count += 1

print(count)