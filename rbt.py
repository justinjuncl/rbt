
class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = None

class RBT():
    def __init__(self):
        self.root = None
        self.nil = Node(None)
        self.nil.color = 'black'
        self.root = self.nil
        self.total = 0

    def search(self,tree,v):
        if tree == self.nil:
            return None
        if v == tree.val:
            return tree
        elif v < tree.val:
            return self.search(tree.left, v)
        else:
            return self.search(tree.right, v)
        return None

    def tree_minimum(self, tree):
        while tree.left != self.nil:
            tree = tree.left
        return tree

    def rotate_left(self,tree,x):
        y = x.right
        x.right = y.left
        if y.left != tree.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == tree.nil:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self,tree,x):
        y = x.left
        x.left = y.right
        if y.right != tree.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == tree.nil:
            tree.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def rb_insert(self,tree,z):
        y = tree.nil
        x = tree.root
        while x != tree.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == tree.nil:
            tree.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = tree.nil
        z.right = tree.nil
        z.color = 'red'
        self.rb_insert_fixup(tree, z)
        self.total = self.total + 1

    def rb_insert_fixup(self,tree,z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(tree, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rotate_right(tree, z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(tree, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rotate_left(tree, z.parent.parent)
        tree.root.color = 'black'

    def rb_transplant(self,tree,u,v):
        if u.parent == tree.nil:
            tree.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete(self,tree,z):
        if z == None:
            return
        y = z
        y_orig_color = y.color
        if z.left == tree.nil:
            x = z.right
            self.rb_transplant(tree, z, z.right)
        elif z.right == tree.nil:
            x = z.left
            self.rb_transplant(tree, z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_orig_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(tree, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(tree, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_orig_color == 'black':
            self.rb_delete_fixup(tree, x)
        self.total = self.total - 1

    def rb_delete_fixup(self,tree,x):
        while x != tree.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(tree, x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.rotate_right(tree, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.rotate_left(tree, x.parent)
                    x = tree.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(tree, x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.rotate_left(tree, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.rotate_right(tree, x.parent)
                    x = tree.root
        x.color = 'black'

    def print(self,tree,level):
        if tree.right != None:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val, tree.color)
        if tree.left != None:
            self.print(tree.left, level + 1)

    def inorder(self,tree):
        if tree == self.nil:
            return
        else:
            self.inorder(tree.left)
            print(tree.val, end=' ')
            self.inorder(tree.right)

    def get_total(self):
        return self.total

    def nb(self,tree):
        if tree == self.nil:
            return 0
        nb = 0
        if tree.color == 'black':
            nb = 1
        return nb + self.nb(tree.left) + self.nb(tree.right)

    def bh(self,tree):
        if tree == self.nil:
            return 0
        bh = 0
        if tree.color == 'black':
            bh = 1
        return bh + self.bh(tree.left)

def main():
    rbt = RBT()
    file = open('input.txt', 'r')
    for line in file:
        value = int(line)
        if value > 0:
            rbt.rb_insert(rbt, Node(value))
        elif value < 0:
            rbt.rb_delete(rbt, rbt.search(rbt.root, -value))
        else:
            print('total = ' + str(rbt.get_total()))
            print('nb = ' + str(rbt.nb(rbt.root)))
            print('bh = ' + str(rbt.bh(rbt.root)))
            rbt.inorder(rbt.root)
            print()
    file.close()

main()