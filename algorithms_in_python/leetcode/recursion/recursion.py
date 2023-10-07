

def out_top_down(i, size):
    if i <= 10:
        out_top_down(i +1, size)
        print(i, end=" ")
def out_bottom_up(i, size):
    if i <= size:
        print(i, end=" ")
        out_bottom_up(i +1, size)


def count(i):
    if i == 0:
        return
    else:
        print(f"{'- ' * i } above {i}")
        count(i -1)
        print(f"{'- ' * i } beneath {i}")




if __name__ == "__main__":
    #out_top_down(1, 10)
    ##print()
    #out_bottom_up(1, 10)

    count(4)


