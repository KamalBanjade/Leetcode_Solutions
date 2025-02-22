
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
       
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]
            
            left_size = root_idx - in_start
            
         
            root.left = build(pre_start + 1, pre_start + left_size, 
                            in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, 
                             root_idx + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)