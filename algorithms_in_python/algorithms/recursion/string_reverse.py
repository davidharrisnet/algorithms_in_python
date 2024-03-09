

def string_reverse(s):
    if len(s) == 1:
        return s
    
    else:
              # the last character       all up to the last character
        return s[len(s)-1] + string_reverse(s[:len(s)-1])
    
              
def string_reverse(s):
    if len(s) == 0:
        return "";
                     
           # all after 1          the first
           # shrinks problem      smallest unit to contribute
    return string_reverse(s[1:]) + s[0]    # o + l + l + e + h
                                       
if __name__ == "__main__":
    string = "hello"
    string_rev = string_reverse(string)
    print(string_rev)