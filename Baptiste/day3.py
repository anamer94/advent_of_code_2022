from functools import reduce

priority_sum = 0
with open("day3.txt", "r") as f:
    for line in f:
        line = line.strip()
        comp1, comp2 = set(c for c in line[:len(line) // 2]), set(c for c in line[len(line) // 2:])

        common = comp1.intersection(comp2)
        assert len(common) == 1

        c = common.pop()
        if c.islower():
            i = ord(c) - 96
        else:
            i = ord(c) - 64 + 26
        priority_sum += i

print(priority_sum)

priority_sum = 0
with open("day3.txt", "r") as f:
    while True:
        lines = [f.readline() for i in range(3)]
        if len(lines[0]) == 0:
            break
        comps = [set(c for c in line.strip()) for line in lines]

        common = reduce(lambda a, b: a.intersection(b), comps)
        assert len(common) == 1, f"common is {common}, comps: {comps}"

        c = common.pop()
        if c.islower():
            i = ord(c) - 96
        else:
            i = ord(c) - 64 + 26
        priority_sum += i

print(priority_sum)
