doors = []

for k in range(0, 100):
    doors.append(0)

for j in range(0, 100):
    for i in range(j, 100, j + 1):
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0

for i in range(0, len(doors)):
    if doors[i] == 1:
        print("%d: %s"%(i + 1, "Open"))