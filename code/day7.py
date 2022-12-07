import re


class Node():
    def __init__(self, data):
        self.child = []
        self.data = data
        self.value = 0
        self.parent = None
    def __str__(self):
        return f"{'*' if self.child else ''} {self.data} {self.value}"


def parcours(node, indent=""):
    print(f"{indent} {node}")
    for childnode in node.child:
        parcours(childnode, indent+"  ")


def value_dir(node):
    res = []
    for childnode in node.child:
        if childnode.child:
            res += value_dir(childnode)
    return [node.value] + res


def remonte_valeur(node):
    if not node.child:
        return node.value
    sum_child_value = 0
    for childnode in node.child:
        sum_child_value += remonte_valeur(childnode)
    node.value = sum_child_value
    return node.value


def find_directory_inf(node, value):
    if node.child:
        childs_values = []
        for childNode in node.child:
            ch_val = find_directory_inf(childNode, value)
            childs_values += ch_val
        if node.value <= value:
            return [node.value] + childs_values
        elif not node.parent:
            return childs_values
        else:
            return childs_values
    else:
        return []


def find_directory_sup(node, value):
    if node.child:
        childs_values = []
        for childNode in node.child:
            ch_val = find_directory_sup(childNode, value)
            childs_values += ch_val
        if node.value > value:
            return [node.value] + childs_values
        elif not node.parent:
            return childs_values
        else:
            return childs_values
    else:
        return []


def compute(inputFile):
    with open(inputFile) as f:
        line = f.readline().strip()
        tree = Node('/')
        actual_Node = tree
        while line:
            if line.startswith('$ cd'):
                dossier = line[5:]
                if dossier == '..':
                    actual_Node = actual_Node.parent
                for node in actual_Node.child:
                    if node.data == dossier:
                        actual_Node = node
            elif line.startswith('$ ls'):
                pass
            else:
                if line.startswith('dir'):
                    dossier = line[4:]
                    node = Node(dossier)
                    node.parent = actual_Node
                    actual_Node.child.append(node)
                else:
                    size = int(re.findall('[0-9]+', line)[0])
                    file = re.findall('[a-zA-Z]+.[a-zA-Z]+|[a-zA-Z]+', line)[0]
                    node = Node(file)
                    node.value = size
                    node.parent = actual_Node
                    actual_Node.child.append(node)

            line = f.readline().strip()
        remonte_valeur(tree)
        #parcours(tree)
        #print(find_directory_inf(tree, 100000))
        return sum(find_directory_inf(tree,100000))


def compute_2(inputFile):
    with open(inputFile) as f:
        line = f.readline().strip()
        tree = Node('/')
        actual_Node = tree
        while line:
            if line.startswith('$ cd'):
                dossier = line[5:]
                if dossier == '..':
                    actual_Node = actual_Node.parent
                for node in actual_Node.child:
                    if node.data == dossier:
                        actual_Node = node
            elif line.startswith('$ ls'):
                pass
            else:
                if line.startswith('dir'):
                    dossier = line[4:]
                    node = Node(dossier)
                    node.parent = actual_Node
                    actual_Node.child.append(node)
                else:
                    size = int(re.findall('[0-9]+', line)[0])
                    file = re.findall('[a-zA-Z]+.[a-zA-Z]+|[a-zA-Z]+', line)[0]
                    node = Node(file)
                    node.value = size
                    node.parent = actual_Node
                    actual_Node.child.append(node)

            line = f.readline().strip()
        remonte_valeur(tree)
        #parcours(tree)
        #print(find_directory_sup(tree, 7E7 - tree.value))
        table_dir = value_dir(tree)
        select = [i if i > (7E7-tree.value) else 7E7 for i in table_dir]
        return min(select)

