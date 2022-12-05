def compute(inputFile):
    with open(inputFile, "r") as f:
        line = f.readline().strip()
        score = 0
        while line:
            mid = len(line)//2
            compartiment1 = set(line[:mid])
            compartiment2 = set(line[mid:])
            items = compartiment1.intersection(compartiment2)
            for item in items:
                if ord(item) >= 97:
                    score += ord(item)-96
                else:
                    score += ord(item)-64+26
            line = f.readline().strip()
        return score


def compute_2(inputFile):
    with open(inputFile, 'r') as f:
        lines = f.readlines()
        score = 0
        for x in range(len(lines)//3):
            elf1 = set(lines[3*x].strip())
            elf2 = set(lines[3*x+1].strip())
            elf3 = set(lines[3*x+2].strip())
            keys = set.intersection(elf1, elf2, elf3)
            for key in keys:
                if ord(key) >= 97:
                    score += ord(key)-96
                else:
                    score += ord(key)-64+26
        return score