class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        def inorder(node):
            if not node:
                return []
            # We will traverse the left subtree
            left = inorder(node.left)
            
            # Traverse the root
            root = [node.val]

            # Traverse the right subtree
            right = inorder(node.right)

            # Combine the result

            return left + root + right

        return inorder(root)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))
