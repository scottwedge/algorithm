"""
Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that
finds the largest key in the tree that is smaller than num. If such a number doesn’t exist, return -1.
Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.
For example:
For num = 17 and the binary search tree below:
alt
Your function would return:
14 since it’s the largest key in the tree that is still smaller than 17.

"""
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    """
    - if the value is bigger than num => go left
    - if the value is smaller than num => go right
    and additionally,
    - but if it has to go right, but there is no right => that is the answer
    - but if it has to go left,  but there is no left  => that means node value is bigger than the num
      we need to go parent, if parent satisfies smaller than num(because it also can be bigger than num) => return that node's val.
    """
    # Time: O(logn)
    # Space: O(1)
    def find_largest_smaller_key(self, num):
        self.biggest = -1

        def helper(node):
            if node.key < num:
                self.biggest = node.key
                if node.right:
                    helper(node.right)
            elif node.key >= num:
                if node.left:
                    helper(node.left)

        helper(self.root)
        return self.biggest

    def insert(self, key):
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while (currentNode is not None):
            if (key < currentNode.key):
                if (currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if (currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);

result = bst.find_largest_smaller_key(5)

print("Largest smaller number is %d " % (result))




















