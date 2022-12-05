def compute(inputFile):
    with open(inputFile, "r") as f:
        line = f.readline().strip()
        score = 0
        while line:
            range1, range2 = line.split(',')
            a, b = range1.split('-')
            x, y = range2.split('-')
            a, b, x, y = int(a), int(b), int(x), int(y)
            if (x<=a and y>=b) or (x>=a and y<=b):
                score += 1
            line = f.readline().strip()
        return score


def compute_2(inputFile):
    with open(inputFile, "r") as f:
        line = f.readline().strip()
        score = 0
        while line:
            range1, range2 = line.split(',')
            a, b = range1.split('-')
            x, y = range2.split('-')
            a, b, x, y = int(a), int(b), int(x), int(y)
            if (b>=x and y >=a):
                score += 1
            line = f.readline().strip()
        return score