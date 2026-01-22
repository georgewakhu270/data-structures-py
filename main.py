from trees import BinarySearchTree

bst = BinarySearchTree()

items = ['anne marie', 'katy perry','ariana grande', 'shania twain', 'jidenna', 'janealle monae', 'charlie puth', 'ed sheeran']

for item in items:
    bst.insert(item)
    
print(bst.root.value)

bst.traversal(bst.root)

bst.search('mariah carey')
