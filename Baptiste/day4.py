full_contains = 0
overlaps = 0
with open("day4.txt", "r") as f:
    for line in f:
        bounds = [int(s) for p in line.split(",") for s in p.split("-")]
        if (bounds[0] <= bounds[2] and bounds[1] >= bounds[3]) or (bounds[0] >= bounds[2] and bounds[1] <= bounds[3]):
            full_contains += 1
        if not (bounds[0] > bounds[3] or bounds[2] > bounds[1]):
            overlaps += 1
print(full_contains)
print(overlaps)
