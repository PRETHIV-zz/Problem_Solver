#it is not like an ordinary binary tree where the lesser andlarger elements are arranged in a manner
#Rather they will give the parent and child node we need to construct a tree first based on the given condition
#and then we have to find the height of the tree
#i used level order traversal for parent node searching in each step since it is going to be the easiest method
# and i used queee method to find unlike ordinary printing technique
#DS Problem_Solve _Pandradhunale oru thani gethu dhana sir
#DS Problem_Solve _Pandradhunale oru thani gethu dhana sir
class Tree:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def findroot(root,n):
    q=[]
    q.append(root)
    while len(q)>0:
        t=q.pop(0)
        if t.data==n:
            return t
        if t.left!=None:
            q.append(t.left)
        if t.right!=None:
            q.append(t.right)
def insertele(root,ins):
    if root.left==None:
        root.left=ins
        return
    if root.right==None:
        root.right=ins
        return
    if ins.data>root.data:
        insertele(root.right,ins)
        return
    else:
        insertele(root.left,ins)
        return
def lvlorder(root):
    q=[]
    q.append(root)
    while len(q)>0:
        t=q.pop(0)
        print(t.data,end=" ")
        if t.left!=None:
            q.append(t.left)
        if t.right!=None:
            q.append(t.right)
def findheight(root):
    if root is None:
        return 0
    else:
        l=findheight(root.left)
        r=findheight(root.right)
        if l>r:
            return l+1
        else:
            return r+1
n,k=map(int,input().split())
root=Tree(None)
find=True
if n==0 and k==0:
    find=False
    h=0
    print(h)
for i in range(k):
    if i==0:
        r,nn=map(int,input().split())
        root=Tree(r)
        newnode=Tree(nn)
        insertele(root,newnode)
    else:
        p,c=map(int,input().split())
        temp=findroot(root,p)
        newnode=Tree(c)
        insertele(temp,newnode)
if find:
    print(findheight(root))
