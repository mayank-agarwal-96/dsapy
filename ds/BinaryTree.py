class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val

class Tree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.left != None):
            self._find(val, node.left)
        elif(val > node.v and node.right != None):
            self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print str(node.v) + ' '
            self._printTree(node.right)