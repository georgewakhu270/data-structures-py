class BinaryTreeNode:
  """This is for a binary tree where each parent node has at most 2 children"""
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  """this class will implement the insertion, search and traversal of a binary tree"""
  def __init__(self):
    self.root = None
    
  def insert(self, key):
    """this will insert a new item to the binary search tree."""
    if self.root == None:
      self.root = BinaryTreeNode(key)
    else:
      self._insert_recursive(self.root, key)
  
  def _insert_recursive(self, curr, key):
    """this is the recursive function that will determine where the new key will be placed"""
    if key < curr.value:
      if curr.left == None:
        curr.left = BinaryTreeNode(key)
      else:
        self._insert_recursive(curr.left, key)
    else:
      if curr.right == None:
        curr.right = BinaryTreeNode(key)
      else:
        self._insert_recursive(curr.right, key)
  
  def search(self, key):
    """this will search for the key in the whole tree"""
    return self._search_recursive(self.root, key)

  def _search_recursive(self, curr, key):
    """this is the recursive function that will search for the key"""
    if curr is None or curr == key:
      return curr is not None
    if key < curr.value:
      return self._search_recursive(curr.left, key)
    return self._search_recursive(curr.right, key)
  
  def traversal(self, curr):
    """this will traverse the whole tree. it will use inorder traversal"""
    if curr:
      self.traversal(curr.left)
      print(curr.value, end=" ")
      self.traversal(curr.right)

class GenericTreeNode:
  """This is for a generic tree where parents have at most more than 2 children"""
  def __init__(self, value):
    self.value = value
    self.children = []

class GenericTree:
  """this is is generic tree"""
  def __init__(self, root_data=None):
    self.root = GenericTreeNode(root_data) if root_data else None
    
  def insert(self, parent, key):
    """the key is added directly to the parent"""
    parent_node = self.search(self.root, parent)
    if parent_node:
      parent_node.children.append(GenericTreeNode(key))
    else:
      print("Parent node does not exists")
      
  def search(self, curr, key):
    '''this will search for the key from the tree'''
    if curr.value == key:
      return curr
    if curr == None:
      return None
      
    for child in curr.children:
      result = search(curr, child)
      if result:
        return result
    return None
    
  def traversal(self, curr, level=0):
    """will utilize depth first search"""
    if curr:
      print(" "*level+"|-- "+str(curr.value))
      for child in curr.children:
        self.traversal(child, level+1)
      
