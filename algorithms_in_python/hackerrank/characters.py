def say_true():
    print("True")

def say_false():
    print("False")

def check_alpha(string):

    alnum = False
    for l in string:
        if l.isalnum():
            alnum = True
            say_true()
            break;
    if not alnum:
        say_false()



    print(string.isalpha())
    print(string.isdigit())
    # line 4
    print(string.islower())
    # line 5
    print(sring.isupper())





if __name__ == "__main__":
    string = "1abb#"
    check_alpha(string)