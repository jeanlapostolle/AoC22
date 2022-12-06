def compute(inputFile):
    with open(inputFile) as f:
        line = f.readline().strip()
        for i in range(len(line)-4):
            if len(set(list(line[i:i+4]))) == 4:
                return i+4


def compute_2(inputFile):
    with open(inputFile) as f:
        line = f.readline().strip()
        for i in range(len(line)-14):
            if len(set(list(line[i:i+14]))) == 14:
                return i+14