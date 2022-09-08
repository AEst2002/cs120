#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)

# See pdf for O(n) justification!
def calculate_sizes(v):
    # Calculate size of trees rooted at v's children if they exist, otherwise they contribute no size.
    if not v:
        return 0
    v.size = 1 + (calculate_sizes(v.left) if v.left else 0) + (calculate_sizes(v.right) if v.right else 0)
    return v.size # Return size of current tree

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    v = r
    while (v.left or v.right):
        left_sz = v.left.size if v.left else 0
        right_sz = v.right.size if v.right else 0
        # check if larger tree is less than size / 2, otherwise move to child from larger tree and try again.
        if max(left_sz, right_sz) < r.size / 2:
            return v
        v = v.left if left_sz > right_sz else v.right
    return v # catch for things like r = None or single node trees.