def push(stack1, x):
    stack1.append(x)


def transfer(stack1, stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())


def pop(stack1, stack2):
    transfer(stack1, stack2)
    return stack2.pop()


def peek(stack1, stack2):
    transfer(stack1, stack2)
    return stack2[-1]


def empty(stack1, stack2):
    return not stack1 and not stack2

stack1 = []
stack2 = []

push(stack1, 1)
push(stack1, 2)

print(peek(stack1, stack2))
print(pop(stack1, stack2))
print(empty(stack1, stack2))