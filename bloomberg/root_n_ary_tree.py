"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # NOT CONSTANT SPACE
        # seen = set()

        # for node in tree:
        #     for child in node.children:
        #         seen.add(child)


        # for node in tree:
        #     if node not in seen:
        #         return node

        
        # THIS METHOD USES ADDITION AND SUBTRACTION. O(1) space complexity
        # EACH CHILD NODE APPEARS EXACRLY TWICE, WHEREAS THE ROOT NODE APPEARS ONLY ONCE
        # SO ADDING AND SUBTRACTING THE CHILD NODES LEAVES EVERYTHING WITH JUST THE ROOT NODE

        sum_val = 0

        # do the addition and subtraction here
        for node in tree:
            sum_val += node.val

            for child in node.children:
                sum_val -= child.val

        
        # the root value is the same as the sum_val
        for node in tree:
            if node.val == sum_val:
                return node 

        