class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add = 0
        total = 0 
        for i,v in enumerate(operations):
            if v == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
            elif v == "C":
                stack.pop()
            elif v == "D":
                stack.append(stack[-1] * 2)
            else: 
                stack.append(int(v))
        return sum(stack)

