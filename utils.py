import numpy as np

def numerize(num: str, outfloat: bool = True, rng: list = [-1e1000, 1e1000], returnstring: bool = True):
    try:
        if outfloat:
            num = float(num)
        else:
            num = int(num)
    except:
        if returnstring:
            return num
        else:
            raise ValueError
    if rng[0] <= num <= rng[1]:
        return num
    else:
        raise ValueError


def readConductor(filepath: str = "conductor.txt") -> np.matrix:
    data=[]
    with open(filepath, 'r') as inputFile:
        for line in inputFile:
            if '>' in line[0]:
                line = line.replace('>', '').replace(' ', '').replace('\n', '')
                line = line.split("|")
                line = [numerize(i) for i in line]
                #print(line)
                data.append(line)
    return np.matrix(data)

