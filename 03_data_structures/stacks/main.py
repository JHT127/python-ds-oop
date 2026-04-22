
from Stack import ArrayStack


def infix_to_postfix(infix_expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = ArrayStack(len(infix_expr))
    postfix = []

    print(f"\nConverting Infix: '{infix_expr}' to Postfix\n")
    print("Step | Char | Stack (Top→Bottom) | Output")
    print("-----|------|---------------------|-------")

    step = 1
    for char in infix_expr:
        if char == ' ':
            continue

        # Print current state BEFORE processing
        stack_str = str([stack.stack[i] for i in range(stack.top + 1)][::-1]) if not stack.is_empty() else "[]"
        output_str = ' '.join(postfix)
        print(f"{step:4} | {char:4} | {stack_str:19} | {output_str}")

        if char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peak() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (not stack.is_empty() and
                   stack.peak() != '(' and
                   precedence.get(char, 0) <= precedence.get(stack.peak(), 0)):
                postfix.append(stack.pop())
            stack.push(char)

        step += 1

    # Pop remaining operators
    while not stack.is_empty():
        postfix.append(stack.pop())

    # Final state
    stack_str = "[]"
    output_str = ' '.join(postfix)
    print(f"{step:4} | {' ':4} | {stack_str:19} | {output_str} (Final)")

    return ' '.join(postfix)


# Test with example
infix_to_postfix("(1 + 2) * 3")