"""
Convert a certain expression like 2+3 to expression in a postfix notation.

The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].

[execution time limit] 4 seconds (py)

[input] array.string expression

An array of tokes of a valid expression in the standard notation.

[output] array.string

Tokens of the expression in the postfix notation.
"""
def toPostFixExpression(e):
    stack_post = []
    stack_op = []
    for i in range(len(e)):
        if e[i] in ["-", "+", "*", "/", "%", "("]:
            if stack_op and stack_op[-1] in ["*", "/", "%"] and e[i] in ["-", "+",]:
                stack_post.append(stack_op.pop())
                stack_op.append(e[i])
            else: stack_op.append(e[i])
        elif e[i] in [")"]:
            while stack_op[-1] != "(":
                stack_post.append(stack_op.pop())
            else: del stack_op[-1]
        else:
            stack_post.append(e[i])
    while stack_op:
        stack_post.append(stack_op.pop())
    return stack_post

print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"]))
                        