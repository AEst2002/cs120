class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    ''' # incorr?
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - (left_size + 1)) #
        return None

    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    # CORR.
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    ''' # SLOW
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.size += 1
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.size += 1
            self.right.insert(key)
        self.calculate_sizes()
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == 'L' and self.left:
            # Grab subtree size for child_side
            subtree_size = self.left.size
            if direction == 'R': # RL

                # Get temp variables for left child of pivot and calculate size of pivot's right child
                temp = self.left.left
                tempsize  = subtree_size - temp.size + (temp.left.size if temp.left else 0)

                # Pointer manipulation for rotation
                self.left.left = temp.right
                temp.right = self.left
                self.left = temp

                # Size reassignment
                self.left.size = subtree_size
                if self.left.right:
                    self.left.right.size = tempsize
            else:                # RR
                temp = self.left.right

                tempsize = subtree_size - temp.size + (temp.left.size if temp.left else 0)

                self.left.right = temp.left
                temp.left = self.left
                self.left = temp

                self.left.size = subtree_size
                if self.left.right:
                    self.left.right.size = tempsize

        if child_side == 'R' and self.right:
            subtree_size = self.right.size
            if direction == 'L': # LR
                temp = self.right.right

                tempsize = subtree_size - temp.size + (temp.left.size if temp.left else 0)

                self.right.right = temp.left
                temp.left = self.right
                self.right = temp

                self.right.size = subtree_size
                if self.right.left:
                    self.right.left.size = tempsize
            else:                # LL
                temp = self.right.left

                tempsize = subtree_size - temp.size + (temp.right.size if temp.right else 0)

                self.right.left = temp.right
                temp.right = self.right
                self.right = temp

                self.right.size = subtree_size
                if self.right.left:
                    self.right.left.size = tempsize
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self