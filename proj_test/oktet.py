# 2**2=4, #2**3=8, #2**4=16, #2**5=32, etc
# Введите 4-й октет маски, например 192
oktet = input("Input a fullmask: 255.255.255.")
numaddr = 256 - int(oktet)
print ("Number of IP addresses: " + str(numaddr))
def stepen():
    if numaddr == 4: return(2)
    elif numaddr == 8: return(3)
    elif numaddr == 16: return(4)
    elif numaddr == 32: return(5)
    elif numaddr == 64: return(6)
    elif numaddr == 128: return(7)
    elif numaddr == 256: return(8)
    else: print('Incoorrect')
stepen()
mask = 32 - stepen()
print ("The mask is: /" + str(mask))