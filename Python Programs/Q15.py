stack = {}
top = -1

def push(value):
    global stack, top
    top += 1
    stack[top] = value

def pop():
    global stack, top
    if is_empty():
        return "Stack is empty!"
    value = stack[top]
    del stack[top]
    top -= 1
    return value

def peek():
    global stack, top
    if is_empty():
        return "Stack is empty!"
    return stack[top]

def is_empty():
    global top
    return top == -1

push(15)
push(30)
print(peek())
print(pop())
print(peek())
print(pop())
print(pop())
