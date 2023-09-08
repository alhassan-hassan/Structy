"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        if not root:
            return ""

        dq = deque([root])
        ans = []

        while dq:
            node = dq.popleft()
            for child in node.children:
                ans.append(str(child.val))
                dq.append(child)
            ans.append("null")

        ans = [str(root.val), "null"] + ans
        return ",".join(ans)


        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        if not data:
            return None
        return Node(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))