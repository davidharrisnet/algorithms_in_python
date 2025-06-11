
# "ace" is a substring of "abcde"

def contains(s,t):
    si = ti = 0
       
    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:                      
            si+=1
           
        ti+=1
    
    return si == len(s)


print(contains("ace", "xxabcdexx"))