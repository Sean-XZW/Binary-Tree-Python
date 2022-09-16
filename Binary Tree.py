class Node:
    def __init__(self, data):
        self.data = data
        self.lechild = None
        self.richild = None

    def getleftPointer(self):
        return self.lechild

    def setleftPointer(self,left):
        self.lechild = left
s
    def setrightPointer(self,right):
        self.richild = right

    def getrightPointer(self):
        return self.richild

    def setdata(self, l):
        self.data = l

    def getdata(self):
        return self.data



class Tree:
    def __init__(self):
        self.root = None
        self.freepointer = None
        self.arr = []
        for i in range(0,9):
            self.arr[i].lechild = i +1
            self.arr[8].lechild = None


#查找
    def search(self, t):



#插入
    def insert(self, a):
        if self.freepointer != None:
            self.newnodepointer == self.freepointer


# 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lechild)
            self.preOrderTraverse(node.richild)


# 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lechild)
            print(node.data)
            self.inOrderTraverse(node.richild)


# 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lechild)
            self.postOrderTraverse(node.richild)
            print(node.data)


a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉找树
bst.inOrderTraverse(bst.root)  # 中序遍历

bst.delete(bst.root, 49)
print()
bst.inOrderTraverse(bst.root)