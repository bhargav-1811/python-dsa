class Bst:
    def __init__(self, key):
        self.key = key
        self.rchild = None
        self.lchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Bst(data)

    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end=" ")

    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inOrder()

    def deleteNode(self, data):
        if self.key is None:
            print("Tree is Empty")
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.deleteNode(data)
            else:
                print("Value not found")
        if self.key < data:
            if self.lchild:
                self.rchild = self.rchild.deleteNode(data)
            else:
                print("Value not found")
        else:
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deleteNode(node.key)
        return self


root = Bst(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)

# root.preOrder()
# print("\n")
# root.inOrder()
# print("\n")
root.inOrder()
print()
root.deleteNode(1)
root.inOrder()
print()
