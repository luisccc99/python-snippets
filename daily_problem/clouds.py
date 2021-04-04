def jumpingOnClouds(clouds):
    steps = 0
    i = 0
    while i < len(clouds) - 1:
        # take 2 steps if it's safe to do so
        if (i + 2) < len(clouds) and clouds[i+2] == 0:
            i += 2
            steps += 1
            continue
        # as default, take 1 step
        i += 1        
        steps += 1
    return steps


if __name__=="__main__":
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
