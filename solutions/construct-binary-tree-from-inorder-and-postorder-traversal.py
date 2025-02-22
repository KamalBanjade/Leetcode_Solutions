class Solution(object):
    def buildTree(self, inorder, postorder):
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(in_start, in_end, post_start, post_end):

            if in_start > in_end:
                return None
            
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            root_idx = inorder_map[root_val]
            
            left_size = root_idx - in_start

            root.left = build(in_start, root_idx - 1, 
                            post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end, 
                             post_start + left_size, post_end - 1)
            
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)