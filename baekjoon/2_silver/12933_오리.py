from sys import stdin


def findDuckCnt(sounds):
    ducks = []
    for sound in sounds:
        if sound == "q":
            for i in range(len(ducks)):
                if ducks[i][-1] == "k":
                    ducks[i] += "q"
                    break
            else:
                ducks.append("q")
        else:
            for i in range(len(ducks)):
                if sound == "u" and ducks[i][-1] == "q":
                    ducks[i] += "u"
                    break
                elif sound == "a" and ducks[i][-1] == "u":
                    ducks[i] += "a"
                    break
                elif sound == "c" and ducks[i][-1] == "a":
                    ducks[i] += "c"
                    break
                elif sound == "k" and ducks[i][-1] == "c":
                    ducks[i] += "k"
                    break
            else:
                return -1

    for duck in ducks:
        if duck[-1] != "k":
            return -1
    return len(ducks)


sounds = stdin.readline().strip()
print(findDuckCnt(sounds))
