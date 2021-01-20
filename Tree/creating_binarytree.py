class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def buildtree():
    data=int(input(" enter integer "))
    if data==-1:
        return None
    root=Node(data)
    root.left=buildtree()
    root.right=buildtree()
    return root
def printtree(root):
    if root==None:
        return root
    print(root.data,end=" ")
    printtree(root.left)
    printtree(root.right)
root=buildtree()
printtree(root)
