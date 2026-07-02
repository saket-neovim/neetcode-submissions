class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add = 0
        total = 0 
        for i in range(len(operations)):
            if operations[i] == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(stack[-1] * 2)
            else: 
                stack.append(int(operations[i]))
        return sum(stack)

