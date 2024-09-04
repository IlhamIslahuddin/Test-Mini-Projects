def using_stack():
    stack = []
    inp = input("What to append to the start: ")
    stack.append(inp)
    for i in range (3):
        new_inp = input(f"Add new item number {i+1}:\n")
        stack.append(new_inp)
    print ("new stack: ")
    print (stack)
    print ("popping most recent value")
    value = stack.pop()
    print (f"popped: {value}")
    print (stack)


if __name__ == "__main__":
    using_stack()
