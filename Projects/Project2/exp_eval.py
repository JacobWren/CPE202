from __future__ import division
from stack_array2 import Stack
import random


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
