
def dec_to_bin2(decimal, result):
    
    if decimal == 0:
       return result
        
    result = f"{decimal % 2}{result}"
    return dec_to_bin2(decimal // 2, result)
    
def dec_to_bin(dec):
    if dec == 1:
       return "1"
    if dec == 0:
        return "0"
   
    # get the remainder
    if dec % 2 == 1:
        return dec_to_bin(dec //2) + "1"
    else:
       return dec_to_bin(dec // 2) + "0"
    
print(dec_to_bin2(8,""))