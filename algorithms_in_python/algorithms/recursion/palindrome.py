
def is_palindrome(the_string):
    if len(the_string) == 0 or len(the_string)  == 1:
        return True
    if the_string[0] == the_string[-1] :
       return is_palindrome(the_string[1:-1])
    else:
        return False
    
    

if __name__ == "__main__":
    s = "yxannaxy"
    p = is_palindrome(s)
    print(p)