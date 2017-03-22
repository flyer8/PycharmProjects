# Аналог условия Select case с использованием словаря
# 2**2=4, #2**3=8, #2**4=16, #2**5=32, etc
addresses = {'4' : "2", '8' : "3", '16' : "4", '32' : "5", '64' : "6", '128' : "7", '256' : "8"}
num = input("Input a number of addresses: (4,8,16,32,64,128,256): ")
#fmask = input("Input a fullmask: 255.255.255.") # Введите 4-й октет маски, например 128
#num = 256 - fmask
if num in addresses:
    stepen = addresses[num]
    mask = 32 - int(stepen)
    print (stepen) #7
    print ("The mask is: " + str(mask))
else:
    print ("Incorrect.")