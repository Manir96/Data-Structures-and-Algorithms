# 1. List / Array
# 2. Function



def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        return "Stack is empty"
    else:
        return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return "Stack is empty"
    else:
        return stack[-1]


def isEmpty(stack):
    return len(stack) == 0


stack = []  # []

push(stack, "a")
push(stack, "b")
push(stack, "c")

print(stack)

print("Top Element: ", peek(stack))

pop(stack)
print(stack)




lst = [1, 2, 3, 4, 5]

print(lst.pop())
print(lst)

pair_parentheses = {
    "(": ")",
    "{": "}",
    "[": "]"
}

print(pair_parentheses["("])


