stack = []
def is_symmetric(sequence):
    opening = "({["
    closing = ")}]"

    for char in sequence:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Несиметрично"
            current_open = stack.pop()
            if opening.index(current_open) != closing.index(char):
                return "Несиметрично"   
    if stack:
        return "Несиметрично"
    return "Симетрично"

# Приклад очікуваного результату:
print(is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_symmetric("( 23 ( 2 - 3)"))
print(is_symmetric("( 11 }"))