class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

""" 
class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        forest = []
        to_delete = set(to_delete)
        
        def delete(node, parent_is_deleted):
            if not node:
                return None
            
            deletion_needed = node.val in to_delete
            if not deletion_needed and parent_is_deleted:
                forest.append(node)
            
            node.left = delete(node.left, deletion_needed)
            node.right = delete(node.right, deletion_needed)
            
            return None if deletion_needed else node
        
        delete(root, True)
        return forest
"""


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        forest = {}
        if not root:
            return []
        forest[root.val] = root

        def find_parent_and_node(root, node_value):
            if not root:
                return None, None
            if root.val == node_value:
                return None, root

            if root.left and root.left.val == node_value:
                return root, root.left

            if root.right and root.right.val == node_value:
                return root, root.right

            parent, node = find_parent_and_node(root.left, node_value)
            if node:
                return parent, node

            return find_parent_and_node(root.right, node_value)

        for del_value in to_delete:

            for r in forest.values():
                parent, node_to_delete = find_parent_and_node(r, del_value)
                if not node_to_delete:
                    continue

                if parent:
                    if parent.left and parent.left.val == del_value:
                        parent.left = None
                    elif parent.right and parent.right.val == del_value:
                        parent.right = None

                if node_to_delete.right:
                    forest[node_to_delete.right.val] = node_to_delete.right

                if node_to_delete.left:
                    forest[node_to_delete.left.val] = node_to_delete.left
                break

            if del_value in forest:
                forest.pop(del_value)

        return forest.values()