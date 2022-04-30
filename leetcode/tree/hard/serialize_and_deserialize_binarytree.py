# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    delim = ','
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        def dfs(n):
            ''' PreOrder DFS'''
            if not n:
                lst.append('N')  # 'N' -> denotes Null|None
                return
            lst.append(str(n.val))
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return Codec.delim.join(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(Codec.delim)
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':  # Null Node
                self.i += 1
                return None 
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # next indicator to pick val
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))