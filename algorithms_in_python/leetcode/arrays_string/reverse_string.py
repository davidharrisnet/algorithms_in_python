def string_reverse(s):

    i = 0
    j = len(s) -1
    sl = list(s)
    while i < j:
        sl[i], sl[j] = sl[j] , sl[i]
        i += 1
        j -= 1
    return "".join(sl)

if __name__ == "__main__":
    s = "abcdefghijklmnop"
    sr = string_reverse(s)
    print(sr)