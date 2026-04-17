class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        permutation = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                result.append(''.join(permutation))
                return

            if open_count < n:
                permutation.append("(")
                backtrack(open_count + 1, close_count)
                permutation.pop()
            if close_count < open_count:
                permutation.append(")")
                backtrack(open_count, close_count + 1)
                permutation.pop()
        
        backtrack(0, 0)

        return result