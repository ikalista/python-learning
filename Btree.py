#建成B tree节点类

class TreeNode:
	def __init__(self, x, name):
		self.name = name
		self.val = x
		self.left = None
		self.right = None
        
n1 = TreeNode(1, "n1")
n2 = TreeNode(0, "n2")
n3 = TreeNode(0, "n3")
n4 = TreeNode(1, "n4")
n5 = TreeNode(0, "n5")

n1.right = n2
n2.left  = n3
n2.right = n4
n4.right = n5


def pruneTree( root: TreeNode ):
    if root.left==None:
        leftIsDeleted = True
        print("左为空")
    else:
        leftIsDeleted = pruneTree(root.left)
        
    if root.right==None:
        rightIsDeleted = True
        print("右为空")
    else:
        rightIsDeleted = pruneTree(root.right)

	if leftIsDeleted and rightIsDeleted and root.val == 0:
        print("删除节点:",root.name)
        print("值:",root.val)
        root = None
        return True
    else: 
        return False

pruneTree(n1)
