with open("day1.txt", "r") as f:
    lines = f.readlines()

curr_weight = 0
elf_weights = []
for line in lines:
    if line == "\n":
        elf_weights.append(curr_weight)
        curr_weight = 0
    else:
        curr_weight += int(line)

print(max(elf_weights))
print(sum(sorted(elf_weights, reverse=True)[:3]))
