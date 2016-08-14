# The script valid for mask more then 24.
# 11111111.11111111.11111111.00000000 = /24
mask = int(input("Enter the mask: ")) # for example 25
#mask = 29 # input mask
hosts = 32 - mask
countaddr = (2**hosts)
counthosts = countaddr - 2
fullmask = 256 - countaddr
print ("Count of addressess: " + str(countaddr))
print ("Count of hosts: " + str(counthosts))
print ("Full mask is: " + "255.255.255." + str(fullmask))