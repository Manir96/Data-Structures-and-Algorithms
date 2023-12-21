# valid parentheses

# -> () - valid
# -> {)(} - Invalid
# -> ()[]{} - Valid
# -> ()[]{}[[] - Valid

# -> (){}[] -> valid parentheses

# - Approach ->  (((])[ - Invalid

# ()[]{}[[]]

# Stack ->

# ())]
# stack ->
# value -> )


# ) -> Peek Element ( -> Open Bracket POP
# ] -> Peek Element [
# } -> Peek Element {

# (}} -> Return valid
# """
def isValid(s):
    pair_parentheses = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    stack = []

    for ch in s:
        if ch in pair_parentheses.keys():
            stack.append(ch)

        else:
            if not stack:
                return False
            else:
                peek_parenthese = stack.pop() # "("

                if pair_parentheses[peek_parenthese] != ch: # pair_parentheses["("] = ) -> ) != )
                    return False

    if stack:
        return False
    return True

print(isValid("([])"))