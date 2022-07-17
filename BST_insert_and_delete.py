#Binary Search Tree



class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




def insert(root,data):
    if(root is None):
        root = Node(data)
        return root
    
    
    
    if(root.data >= data):
        root.left = insert(root.left,data)
       
    
    else:
        root.right = insert(root.right,data)
    
    
    return root
        



def inorder(root):
    if(root is None):
        return 
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
    


def search(root,data):
    
    if(root is None):
        return False
    
    if(root.data == data):
        return True
    
    
    if(root.data > data):
        return search(root.left,data)
    
    else:
        return search(root.right,data)


def delete(root,data):
    
    if(root is None):
        return root
    
    if(root.data == data):
        if(root.left is None and root.right is None):
            root = None
            return root
        
        elif(root.left and root.right is None):
            node = root.left
            root = None
            return node
        
        elif(root.right and root.left is None):
            node = root.right
            root = None
            return node
        
        else:
            node = successor(root.right)
            root.data = node.data
            root.right = delete(root.right,node.data)
    
    
    if(root.data > data):
        root.left = delete(root.left,data)
    
    
    else:
        root.right = delete(root.right,data)
        
    
    return root
    

def successor(root):
    
    temp = root
    while(temp.left):
        temp = temp.left
    
    return temp    





root = insert(None,10)
root = insert(root,20)
root = insert(root,30)
root = insert(root,5)
root = insert(root,7)
root = insert(root,15)

inorder(root)

print(search(root,2))
print(search(root,7))
print(search(root,30))
print(search(root,15))


root = delete(root,20)
inorder(root)
