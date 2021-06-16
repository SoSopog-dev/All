import random
from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyzæøå "
p_al = ""
pairs = {}
p_al = list(p_al)
if int(input("Generate? 1 = Yes 2 = No")) == 1:
    seed = randint(1,100)
    random.seed(seed)
    for letter in alphabet:
        newletter = alphabet[randint(0,29)]
        while newletter in p_al :
            newletter = alphabet[randint(0,29)]
        p_al.append(newletter)
        pairs[letter]= newletter
print (seed)
p_al = ""
