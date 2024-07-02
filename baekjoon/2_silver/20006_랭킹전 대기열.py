from sys import stdin

p, m = map(int, stdin.readline().split())
rooms = []
for _ in range(p):
    l, n = stdin.readline().split()
    l = int(l)

    entered = False
    for room in rooms:
        tl = room[0][0]
        if len(room) < m and abs(tl - l) <= 10:
            room.append((l, n))
            entered = True
            break

    if not entered:
        rooms.append([(l, n)])

for room in rooms:
    room.sort(key=lambda x: x[1])
    print("Started!" if len(room) == m else "Waiting!")
    for l, n in room:
        print(l, n)
