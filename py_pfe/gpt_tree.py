import copy
from collections import deque
import sys
sys.setrecursionlimit(10**9)

def reverse(s):
    if len(s) == 0:
        return s
    else:
        s0 = s[0]
        if s0.islower():
            s0 = s0.upper()
        elif s0.isupper():
            s0 = s0.lower()
        return s0 + reverse(s[1:])

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.chemin = 0

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def compare(self, combinaison):
        for i in range(len(combinaison)):
            if self.data[i] != combinaison[i]:
                return False
        return True

    def recherche(self, combinaison):
        if self.compare(combinaison):
            return self.chemin
        if self.children:
            for child in self.children:
                i = child.recherche(combinaison)
                if i != -1:
                    return i
        return -1

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree(root, racine, y):
    j=0
    file = deque([root])
    combinaisons = set([root.data])
    while file:
        node = file.popleft()
        combinaison = node.data
        for i in range(len(combinaison)-y+1):
            a = combinaison[i:i+y]
            b = reverse(a)
            c = combinaison[:i] + b + combinaison[i+y:]
            d = b[::-1]
            e = c[:i] + d + c[i+y:]
            if e not in combinaisons:
                j=j+1
                child = TreeNode(e)
                node.add_child(child)
                child.chemin = node.chemin*10+i+1
                combinaisons.add(e)
                file.append(child)
    print (j)

x = input("Entrer la chaine de char\n")
y = int(input("Entrer le nombre de cub adjacent a tourner\n"))
a1 = TreeNode(x)
build_tree(a1, a1, y)
a1.print_tree()

