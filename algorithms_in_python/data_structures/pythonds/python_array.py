from array import array

def do_array():
    a = array('I')
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)

    print(a)


if __name__ == "__main__":
    do_array()