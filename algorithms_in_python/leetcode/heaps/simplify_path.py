
def simplify_path(path):
    parts = path.split('/')
    abspath = []
    for p in parts:
      if len(p) > 0:
        if p == "..":
            if len(abspath) > 0:
                abspath.pop(len(abspath)-1)
                abspath.pop(len(abspath)-1)        
        elif p != ".":
            abspath.append("/")
            abspath.append(p)
    if len(abspath) == 0:
        abspath.append("/")
        
    return "".join(abspath)
                        
    
path = "/a/./b/../../c/"

abspath = simplify_path(path)
print(abspath)
    
    