
from trees import BinarySearchTree, GenericTree
from graphs import Graph

bst = BinarySearchTree()

items = ['anne marie', 'katy perry','ariana grande', 'shania twain', 'jidenna', 'janealle monae', 'charlie puth', 'ed sheeran']

for item in items:
    bst.insert(item)
    
print(bst.root.value)

bst.traversal(bst.root)

bst.search('mariah carey')

print("")

gt = GenericTree("CEO")
gt.insert("CEO", "VP of Sales")
gt.insert("CEO", "VP of Engineering")
gt.insert("VP of Engineering", "Tech Lead")
gt.insert("VP of Engineering", "QA Manager")
gt.insert("Tech Lead", "Software Engineer")

gt.traversal(gt.root)

g = Graph()
nodes = ['A', 'B', 'C', 'D', 'E']
for n in nodes: g.add_vertex(n)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print("DFS Recursive starting from A:")
g.dfs_recursive('A')
print("\nBFS starting from A")
g.bfs('A')
