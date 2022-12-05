from parse import *


def compute(inputFile):
    with open(inputFile, 'r') as f:
        #construct piles
        nbDePiles = 9
        piles = [[] for _ in range(nbDePiles)]
        line = f.readline()[:-1]
        while not line.startswith(" 1 "):
            for i in range(len(line)//4 +1 ):
                caract = line[4*i+1: 4*i+2]
                if not caract == ' ':
                    piles[i].append(caract)
            line = f.readline()[:-1]
        f.readline() # Passe le blanc
        line = f.readline().strip()
        while line:
            parseResult = parse("move {} from {} to {}", line)
            quantite = int(parseResult[0])
            depuis = int(parseResult[1])-1
            vers = int(parseResult[2])-1

            tmpList = []
            for _ in range(quantite):
                item = piles[depuis].pop(0)
                piles[vers].insert(0,item)

            line = f.readline().strip()

        return "".join([pile[0] if len(pile) > 0 else "" for pile in piles])


def compute_2(inputFile):
    with open(inputFile, 'r') as f:
        #construct piles
        nbDePiles = 9
        piles = [[] for _ in range(nbDePiles)]
        line = f.readline()[:-1]
        while not line.startswith(" 1 "):
            for i in range(len(line)//4 +1 ):
                caract = line[4*i+1: 4*i+2]
                if not caract == ' ':
                    piles[i].append(caract)
            line = f.readline()[:-1]
        f.readline() # Passe le blanc
        line = f.readline().strip()
        while line:
            parseResult = parse("move {} from {} to {}", line)
            quantite = int(parseResult[0])
            depuis = int(parseResult[1])-1
            vers = int(parseResult[2])-1

            tmpList = []
            for _ in range(quantite):
                item = piles[depuis].pop(0)
                tmpList.insert(0,item)

            for _ in range(quantite):
                item = tmpList.pop(0)
                piles[vers].insert(0, item)

            line = f.readline().strip()

        return "".join([pile[0] if len(pile) > 0 else "" for pile in piles])