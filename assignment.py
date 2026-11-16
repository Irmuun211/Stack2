# Exercise 1
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)


def Push(Item):
    global Stack, TopOfStack
    if TopOfStack == 7:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return -1
    x = Stack[TopOfStack]
    TopOfStack -= 1
    return x

# Exercise 2
def ShowStack():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return ""
    s = ""
    for i in range (TopOfStack, -1 , -1):
        s = s + str(Stack[i])
        if i > 0:
            s = s + " "
    return s

# Exercise 3
def DecimalToBinary(Number):
    global Stack, TopOfStack
    TopOfStack = -1
    if Number == 0:
        return '0'
    while Number>0:
        Push(Number % 2)
        Number = Number // 2
    d = ""
    while TopOfStack != -1:
        x = Pop()
        d = d + str(x) + ""
    return d

# Exercise 4
def Editor(Commands):
    global Stack, TopOfStack
    TopOfStack = -1
    for i in range(len(Commands)):
        parts = Commands[i].split(" ")
        if parts[0] == "type":
            Push(parts[1])
        elif parts[0] == "undo":
            Pop()
    a = ""
    for i in range(0, TopOfStack+1, 1):
        a = a + Stack[i]
    return a
