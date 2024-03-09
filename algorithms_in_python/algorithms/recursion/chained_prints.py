def A():
    return "a "  + B()

def B():
    return "b " + C()

def C():
    return "c"

print(A())
    