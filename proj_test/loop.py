for i in range(1,21):
    f = open("text.txt","w")
    f.write("This is line %d\r\n" % (i+1))
    f.close()