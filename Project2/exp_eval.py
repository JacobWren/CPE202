from __future__ import division
from stack_array2 import Stack

import random
# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack = Stack(30) # Empty stack, cap = 30
    expression_list = input_str.split() # Convert input string into a list
    for i in expression_list:
        if (i != "+" and i != "-" and i != "*" and i != "/" and i != "**" and i != "<<" and i != ">>" ):
            try:
                float(i)
                try:
                    stack.push(int(i))
                except:
                    stack.push(float(i))  # push number onto stack
            except:
                raise PostfixFormatException("Invalid token")

        else:
            try:
                operand2 = stack.pop() # this is the second operand because of division and exponentiation
                operand1 = stack.pop()
            except:
                raise PostfixFormatException("Insufficient operands")
            if i == "/" and operand2 == 0:
                raise ValueError
            if (i == "<<" or i == ">>") and (type(operand2) == float or type(operand1) == float):
                raise PostfixFormatException("Illegal bit shift operand")
            answer = calculator(i, operand1, operand2)
            stack.push(answer)
    if stack.num_items == 1:
        return stack.pop()
    elif stack.num_items > 1:
        raise PostfixFormatException("Too many operands")

# does the algebra and returns the result!
def calculator(operator, operand1, operand2):
    if operator == "<<":
        return operand1 << operand2
    elif operator == ">>":
        return operand1 >> operand2
    elif operator == "**":
        return operand1 ** operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2

#print(postfix_eval("10.2 11 >>"))



""" 
Python3 program to evaluate a prefix expression. 
"""


def is_operand(c):
    """
    Return True if the given char c is an operand, e.g. it is a number
    """
    return c.isdigit()


def evaluate(expression):
    """
    Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid.
    """
    stack = []

    # iterate over the string in reverse order
    for c in expression[::-1]:

        # push operand to stack
        if is_operand(c):
            stack.append(int(c))

        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            o2 = stack.pop()

            if c == '+':
                stack.append(o1 + o2)

            elif c == '-':
                stack.append(o1 - o2)

            elif c == '*':
                stack.append(o1 * o2)

            elif c == '/':
                stack.append(o1 / o2)

    return stack.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    stack = Stack(30)
    rpn = []
    expression_list = input_str.split()
    for i in expression_list:
        try:
            float(i)
            rpn.append(i)
        except:
            if i == "(":
                stack.push(i)
            elif i == ")":
                while stack.items[stack.num_items-1] != "(":
                    rpn.append(stack.pop())
                stack.pop()
            elif operator(i):
                while operator(stack.items[stack.num_items-1]) and ( (i == "**" and precedence_dict_2(i, stack.items[stack.num_items-1]))
                    or  (left_assoc(i) and precedence_dict(i, stack.items[stack.num_items - 1]))):
                    rpn.append(stack.pop())
                stack.push(i)
    while stack.num_items > 0:
            rpn.append(stack.pop())
    return ' '.join(rpn)




def operator(op):
    """this function returns true if operator (op) is an operator and false otherwise"""
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "**" or op == "<<" or op == ">>" ):
        return True
    return False

def left_assoc(op):
    """this function returns true if operator (op) is left associative and false otherwise"""
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "<<" or op == ">>" ):
        return True
    return False

def precedence_dict(op1, op2):
    """this function returns true if precedence of op1 is less or equal to the precedence of op2"""
    precedence = {}
    precedence[">>"] = 5
    precedence["<<"] = 5
    precedence["**"] = 4
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    if precedence[op1] <= precedence[op2]:
        return True
    return False

def precedence_dict_2(op1, op2):
    """this function returns true if precedence of op1 is strictly less than the precedence of op2"""
    precedence = {}
    precedence[">>"] = 5
    precedence["<<"] = 5
    precedence["**"] = 4
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    if precedence[op1] < precedence[op2]:
        return True
    return False

#print(infix_to_postfix("3 << 4 ** 2 / ( 1 - 5 ) ** 2 ** 3"))



def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)
    rpn = []
    expression_list = input_str.split()
    j = len(expression_list) - 1
    for i in range(j, -1, -1): # reverse order
        try:
            float(expression_list[i])
            stack.push(expression_list[i])
        except:
            if operator(expression_list[i]):
                op1 = stack.pop()
                op2 = stack.pop()
                concat = op1 + " " + op2 + " " + expression_list[i]
                stack.push(concat)
    while stack.num_items > 0:
            rpn.append(stack.pop())
    return ' '.join(rpn)

print(infix_to_postfix("( 3 + 2 ) - 5 * 6 / 3"))
#['a', 'b', 'c', '^', 'd', 'e', '-', '^', 'f', 'g', 'h', '*', '+', '*', '+', 'i', '-']

#print(postfix_eval("4 7 5 + 6 / 3 * -"))

##################



OPERATORS = set(['+', '-', '*', '/', '(', ')', '**', '<<', '>>'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '**':3, '>>':4, '<<':4}





### INFIX ===> POSTFIX ###
'''
1)Fix
a
priority
level
for each operator.For example, from high to low:
    3. - (unary negation)
2. * /
1. + - (subtraction)
2) If
the
token is an
operand, do
not stack
it.Pass
it
to
the
output.
3) If
token is an
operator or parenthesis:
3.1) if it is '(', push
3.2) if it is ')', pop until '('
3.3) push the incoming operator if its priority > top operator; otherwise pop.
* The popped stack elements will be written to output.
4) Pop the remainder of the stack and write to the output (except left
parenthesis)
'''
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: output += stack.pop()
    print(output)
    return output


### POSTFIX ===> INFIX ###
'''
1) When
see
an
operand, push
2) When
see
an
operator, pop
out
two
numbers, connect
them
into
a
substring and push
back
to
the
stack
3) the
top
of
the
stack is the
final
infix
expression.
'''
def postfix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in formula:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            if prev_op and len(a) > 1 and PRIORITY[ch] > PRIORITY[prev_op]:
                # if previous operator has lower priority
                # add '()' to the previous a
                expr = '('+a+')' + ch + b
            else:
                expr = a + ch + b
            stack.append(expr)
            prev_op = ch
    print(stack[-1])
    return stack[-1]


### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(exp_stack[-1])
    return exp_stack[-1]


### PREFIX ===> INFIX ###
'''
Scan
the
formula
reversely
1) When
the
token is an
operand, push
into
stack
2) When
the
token is an
operator, pop
out
2
numbers
from stack, merge

them and push
back
to
the
stack
'''
def prefix_to_infix(formula):
    stack = []
    prev_op = None
    for ch in reversed(formula):
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if prev_op and PRIORITY[prev_op] < PRIORITY[ch]:
                exp = '('+a+')'+ch+b
            else:
                exp = a+ch+b
            stack.append(exp)
            prev_op = ch
    print(stack[-1])
    return stack[-1]


'''
Scan
the
formula:
1) When
the
token is an
operand, push
into
stack;
2) When
an
operator is encountered:
2.1) If
the
operator is binary, then
pop
the
stack
twice
2.2) If
the
operator is unary(e.g.unary
minus), pop
once
3) Perform
the
indicated
operation
on
two
poped
numbers, and push
the
result
back
4) The
final
result is the
stack
top.
'''
def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[ch]
            stack.append(c)
    print(stack[-1])
    return stack[-1]


def evaluate_infix(formula):
    return evaluate_postflix(inflix_to_postfix(formula))


'''
Whenever
we
see
an
operator
following
by
two
numbers,
we
can
compute
the
result.
'''
def evaluate_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps)-2):
            if exps[i] in OPERATORS:
                if not exps[i+1] in OPERATORS and not exps[i+2] in OPERATORS:
                    op, a, b = exps[i:i+3]
                    a,b = map(float, [a,b])
                    c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[op]
                    exps = exps[:i] + [c] + exps[i+3:]
                    break
        print(exps)
    return exps[-1]


if __name__ == '__main__':
    infix_to_postfix('(3+2)-5*6/3')
    #infix_to_prefix('1+(3+4*6+6*1)*2/3')
    #evaluate_inflix('1+(3+4*6+6*1)*2/3')
    #evaluate_postfix('1346*+61*+2*3/+')
    #evaluate_prefix('+1/*++3*46*6123')
    #postfix_to_infix('1346*+61*+2*3/+')
    #prefix_to_infix('+1/*++3*46*6123')
