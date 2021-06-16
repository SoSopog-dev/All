a = 0
counter = 0
lisst = []
femcounter = 0
for i in range(int(input())):
    if counter == 1:
        if  not femcounter == 5:
            lisst.append(a)
            
            
            


        a += 1
        counter = 0
        femcounter += 1
        print(femcounter)

    else:
        a += 1
        counter = 1
        femcounter += 1
        print(femcounter)
    if femcounter == 5:
            femcounter = 0
print (lisst)
