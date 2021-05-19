class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    
def inordersucc(root):
    
    temp = root
    while(temp.left):
        temp = temp.left
    
    return temp

  
  
  
    
def insert(root,data):
    if(root is None):
        root = Node(data)
        return root
    
    if(root.data >= data):
        root.left = insert(root.left,data)
    
    else:
        root.right = insert(root.right,data)
    
    return root
     
    
    
        
def delete(root,data):
    
    if(root is None):
        return root
    
    
    if(root.data == data):
        if(root.left is None and root.right is None):
            root = None
            return root
        
        elif(root.right is None):
            temp = root.left
            root = None
            return temp
        
        
        elif(root.left is None):
            temp = root.right
            root = None
            return temp
        
        else:
            
            x = inordersucc(root.right)
            root.data = x.data
            
            root.right = delete(root.right,x.data)
            
    
    elif(root.data >= data):
        root.left = delete(root.left,data)
    
    else:
        root.right = delete(root.right,data)
            
        
    return root    
     
    
    
    
def inorder(root):
    if(root is None):
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
root = None
root = insert(root,12)
root = insert(root,14)
root = insert(root,16)
root = insert(root,10)
root = insert(root,8)
root = insert(root,9)
inorder(root)
root = delete(root,10)
inorder(root)
