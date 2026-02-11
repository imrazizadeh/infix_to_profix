import re

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTreeProject:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def tokenize(self, expression):
        return re.findall(r'\d+|[+\-*/()]', expression)

    def infix_to_postfix(self, expression):
        tokens = self.tokenize(expression)
        output = []
        stack = Stack()

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in self.operators:
                while (not stack.is_empty() and stack.peek() != '(' and
                       self.precedence.get(stack.peek(), 0) >= self.precedence[token]):
                    output.append(stack.pop())
                stack.push(token)
        
        while not stack.is_empty():
            output.append(stack.pop())
            
        return output

    def build_tree(self, postfix_list):
        stack = Stack()

        for token in postfix_list:
            if token.isdigit():
                stack.push(Node(token))
            else:
                new_node = Node(token)
                new_node.right = stack.pop()
                new_node.left = stack.pop()
                stack.push(new_node)
        
        return stack.pop()

    def evaluate(self, node):
        if node.left is None and node.right is None:
            return int(node.value)

        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/': return left_val / right_val

if __name__ == "__main__":
    project = ExpressionTreeProject()
    
    print("--- Expression Tree Project ---")
    user_input = input("Enter Infix expression: ")
    
    try:
        postfix_tokens = project.infix_to_postfix(user_input)
        postfix_str = "".join(postfix_tokens)
        print(f"postfix: {postfix_str}")
        
        root = project.build_tree(postfix_tokens)
        
        result = project.evaluate(root)
        print(f"result: {result}")
        
    except Exception as e:
        print(f"Error: {e}")