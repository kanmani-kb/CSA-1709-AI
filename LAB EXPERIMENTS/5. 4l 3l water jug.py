
jug4 = 0
jug3 = 0

print("Initial State: 4L =", jug4, "3L =", jug3)

while jug4 != 2:
    if jug4 == 0:
        jug4 = 4
        print("Fill 4L jug:", jug4, jug3)

    elif jug3 < 3 and jug4 > 0:
        transfer = min(jug4, 3 - jug3)
        jug4 -= transfer
        jug3 += transfer
        print("Pour 4L into 3L:", jug4, jug3)

    elif jug3 == 3:
        jug3 = 0
        print("Empty 3L jug:", jug4, jug3)

    elif jug4 == 2:
        break

print("Goal Reached!")
print("Final State: 4L =", jug4, "3L =", jug3)
