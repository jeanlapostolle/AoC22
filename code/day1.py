def compute(inputPath):
    with open(inputPath, "r") as f:
        line = f.readline()
        list_elfs = []
        actual_elf = 0

        while line:
            if line == "\n":
                list_elfs.append(actual_elf)
                actual_elf = 0
            else:
                actual_elf += int(line)
            line = f.readline()
        list_elfs.append(actual_elf)

        return max(list_elfs)


def compute_2(inputPath):
    with open(inputPath, "r") as f:
        line = f.readline()
        list_elfs = []
        actual_elf = 0

        while line:
            if line == "\n":
                list_elfs.append(actual_elf)
                actual_elf = 0
            else:
                actual_elf += int(line)
            line = f.readline()
        list_elfs.append(actual_elf)

        max_1 = max(list_elfs)
        list_elfs.remove(max_1)
        max_2 = max(list_elfs)
        list_elfs.remove(max_2)
        max_3 = max(list_elfs)
        return max_1+max_2+max_3