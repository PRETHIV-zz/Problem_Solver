#Lowest Common Ancestor
class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def insert(root,ins):
    if ins.data>root.data and root.right!=None:
        insert(root.right,ins)
    elif ins.data<=root.data and root.left!=None:
        insert(root.left,ins)
    if ins.data>root.data and root.right==None:
        root.right=ins
        return
    elif ins.data<=root.data and root.left==None:
        root.left=ins
        return
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def lcafinder(root,n1,n2):
    if root is None:
        return None
    if root.data>n1 and root.data>n2:
        return lcafinder(root.left,n1,n2)
    if root.data<n1 and root.data<n2:
        return lcafinder(root.right,n1,n2)
    return root.data

n=int(input())
a=list(map(int,input().split()))
l,r1=map(int,input().split())
r=Node(a[0])
for i in  range(1,n):
    nn=Node(a[i])
    insert(r,nn)
#inorder(r)
print(lcafinder(r,l,r1))
