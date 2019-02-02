#i am new biee to DS but i tried my best
#Chk_Sum_tree
class Tree:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
def insertele(root,nn):
    if root.left==None:
        root.left=nn
        return
    elif root.right==None:
        root.right=nn
        return
    if nn.data<root.data:
        insertele(root.left,nn)
    else:
        insertele(root.right,nn)
def findroot(root,nn):
    if root is None:
        return None
    else:
        q=[]
        q.append(root)
        while len(q)>0:
            temp=q.pop(0)
            if temp.data==nn:
                return temp
            else:
                if temp.left!=None:
                    q.append(temp.left)
                if temp.right!=None:
                    q.append(temp.right)
def lvlorder(root,d=False):
    if root is None:
        return None
    else:
        q=[]
        ans=[]
        val=[]
        q.append(root)
        while len(q)>0:
            temp=q.pop(0)
            if d:
                val.append(temp.data)
            else:
                ans.append(temp)
            print(temp.data,end=" ")
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)
        if d:
            return val
        else:
            return ans
def calcsum(root):
    if root.left==None and root.right==None:
        return root.data
    elif root.left==None and root.right!=None:
        return root.data+calcsum(root.right)
    elif root.right==None and root.left!=None:
        return root.data+calcsum(root.left)
    else:
        return root.data+calcsum(root.left)+calcsum(root.right)

def passroot(root):
    l=0
    r=0
    if root.left!=None:
        l=calcsum(root.left)
    else:
        l=0
    if root.right!=None:
        r=calcsum(root.right)
    else:
        r=0
    s=l+r
    if s==0:
        return root.data
    else:
        return s
n,m=map(int,input().split())
root=Tree(None)
for i in range(m):
    if i==0:
        nn,val=map(int,input().split())
        root.data=nn
        newnode=Tree(val)
        insertele(root,newnode)
    else:
        nn,val=map(int,input().split())
        newnode=Tree(val)
        it=findroot(root,nn)
        insertele(it,newnode)
sa=passroot(root)
if sa==root.data:
    print("YES")
else:
    print("NO")
