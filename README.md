# Expression Tree Project

A simple Python implementation of an **Expression Tree** that:

- Converts an **Infix expression** to **Postfix notation**
- Builds an **Expression Tree**
- Evaluates the expression result

---

## 📌 Features

- Stack implementation using a Python list
- Infix → Postfix conversion (Shunting Yard algorithm logic)
- Expression Tree construction from Postfix
- Recursive evaluation of the tree
- Supports operators: `+`, `-`, `*`, `/`
- Supports parentheses

---

## 📂 Project Structure

- `Stack` → Custom stack implementation  
- `Node` → Binary tree node  
- `ExpressionTreeProject` → Main logic (conversion, tree building, evaluation)

---

## 🧠 How It Works

### 1️⃣ Tokenization

The expression is tokenized using regular expressions:

```python
re.findall(r'\d+|[+\-*/()]', expression)
```

---

This extracts:

- Multi-digit numbers
- Operators
- Parentheses

---

### 2️⃣ Infix to Postfix Conversion

Uses:

- A stack for operators
- Operator precedence rules:
  - `+`, `-` → precedence 1
  - `*`, `/` → precedence 2

Returns a list of postfix tokens.

---

### 3️⃣ Building the Expression Tree

From postfix expression:

- If token is a number → create node and push to stack
- If token is operator →
  - Pop two nodes
  - Create operator node
  - Attach left & right children
  - Push back to stack

Final stack element → Root of the tree

---

### 4️⃣ Evaluation

Recursive traversal:

- If leaf node → return integer value
- Otherwise:
  - Evaluate left subtree
  - Evaluate right subtree
  - Apply operator

---

## 💻 Full Source Code

```python
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
```

---

## ▶️ Example Run

```
--- Expression Tree Project ---
Enter Infix expression: 3+5*2
postfix: 352*+
result: 13
```

---

## ⚠️ Notes

- Only integer operands are supported.
- Division returns float values.
- No support for negative numbers or exponentiation.
- Input must be a valid infix expression.

---

## 🚀 Possible Improvements

- Add support for:
  - Floating point numbers
  - Exponent operator (`^`)
  - Unary minus
- Add tree visualization
- Improve error handling
- Add unit tests

---

## 📜 License

This project is for educational purposes.
