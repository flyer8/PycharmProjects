# 2**2=4, #2**3=8, #2**4=16, #2**5=32, etc
def mask():
    num = int(input("Enter the number: "))
    if num == 4: return(2)
    elif num == 8: return(3)
    elif num == 16: return(4)
    elif num == 32: return(5)
    elif num == 64: return(6)
    elif num == 128: return(7)
    elif num == 256: return(8)
    else: print('Incoorrect')
print (mask())
m = 32 - 7
print (m)