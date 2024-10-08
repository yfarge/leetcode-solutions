from collections import defaultdict, deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return

            if depth == len(answer):
                answer.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        answer = []
        dfs(root, 0)
        return answer


# Iterative
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = defaultdict(int)

        if not root:
            return right_side.values()

        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            right_side[depth] = node.val

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return right_side.values()
