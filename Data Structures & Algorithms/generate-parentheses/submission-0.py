class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path=[]
        result = []
        def backtracking(path, open, close):
            if open == n and close == n:
                result.append("".join(path))
                return
            if open < n:
                path.append("(")
                backtracking(path, open + 1, close)
                path.pop()
            if close < open:
                path.append(")")
                backtracking(path, open, close + 1)
                path.pop() 
        backtracking(path, 0, 0) 
        return result           
