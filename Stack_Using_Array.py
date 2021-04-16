# Implement stack(Both Push and Pop) and Print the Output #
#stack work on FIFO( First Come First Out) statement#
from sys import maxsize
# Create and array stack and return #
def create_Stack():
    stack = []
    return stack
# check whether if is empty #
def is_Empty(stack):
    return len(stack) == 0
# push function #
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")
# pop function #
def pop(stack):
    if is_Empty(stack):
        return str(-maxsize-1)

    return stack.pop()
# top function and check traversal #
def peek(stack):
    if is_Empty(stack):
       return str(-maxsize -1)
    return stack[len(stack)-1]
# array of stack #
stack = [10, 20, 30, 40, 50, 60, 70, 80]
pop(stack)      # pop the element from stack #
print(stack)

pop(stack)
print(stack)

pop(stack)
print(stack)

push(stack, str(100))       # push the element in the stack #
print(stack)        # print #

