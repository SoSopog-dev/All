a = input()
s = list(a)
s = "".join(s)

def bytt(letter, letter_value, s):
    for i in range(len(a)):
        len_letter = (len(letter))-2
        if not s.find(letter)== -1:
            pos_letter = s.find(letter) + 1
            print (pos_letter)
            if s.find(letter) == -1 :
                break
            counter = 0
            s = list(s)
            s[pos_letter] = letter_value
            for i in range(len_letter - 1):
                s[pos_letter + 1 + counter] = ""
                counter = counter + 1
        s = "".join(s)
        if s.find(letter) == -1:
            print(s)
            return (s)






def tierbytt(tenletter, ten_value, s):
    len_tenletter = (len(tenletter)) -1
    sL1 = ("en ")
    sL2 = ("to ")
    sL3 = ("tre ")
    sL4 = ("fire ")
    sL5 = ("fem ")
    sL6 = ("seks ")
    sL7 = ("syv ")
    sL8 = ("åtte ")
    sL9 = ("ti ")
    sL1_value = ("1")
    sL2_value = ("2")
    sL3_value = ("3")
    sL4_value = ("4")
    sL5_value = ("5")
    sL6_value = ("6")
    sL7_value = ("7")
    sL8_value = ("8")
    sL9_value = ("9")
    L_sL1 = (len(sL1))
    L_sL2 = (len(sL2))
    L_sL3 = (len(sL3))
    L_sL4 = (len(sL4))
    L_sL5 = (len(sL5))
    L_sL6 = (len(sL6))
    L_sL7 = (len(sL7))
    L_sL8 = (len(sL8))
    L_sL9 = (len(sL9))
    print (tenletter)
    for i in range(len(a)):
        if not s.find(tenletter) == -1:
            pos_tenletter = s.find(tenletter) + 1
            print (pos_tenletter)
            stest2 = s[pos_tenletter + len_tenletter] + s[pos_tenletter + len_tenletter + 1] +  s[pos_tenletter + len_tenletter + 2]
            print (stest)
            stest3 = s[pos_tenletter + len_tenletter] + s[pos_tenletter + len_tenlettter + 1] + s[pos_tenletter + len_tenletter + 2] + s[pos_tenletter + len_tenletter + 3]
            pos_singleletter = pos_tenletter + len_tenletter
            if stest == sL1:
                if not s.find(sL1) == -1:
                    counter = 0
                    if s.find(tenletter) == -1:
                        return s
                    if s.find(sL1) == -1:
                        return s
                    s = list(s)
                    print (pos_tenletter)
                    s[pos_tenletter] = ten_value
                    s = "".join(s)
                    print(s)
                    s = list(s)
                    for i in range(len_tenletter - 1):
                        s[pos_tenletter + 1 + counter] = ""
                        counter = counter + 1
                    counter = 0
                    s[pos_singleletter] = sL1_value
                    for i in range(L_sL1 - 1):
                        s[pos_singleletter + 1 + counter] = ""
                        counter = counter + 1
                    s[pos_singleletter + 1] = ""
                    s = "".join(s)
                    print (s)
                    if s.find(tenletter) == -1:
                        return (s)
            if stest == sL2:
                if not s.find(sL2) == -1:
                    counter = 0
                    if s.find(tenletter) == -1:
                        return s
                    if s.find(sL2) == -1:
                        return s
                    s = list(s)
                    print (pos_tenletter)
                    s[pos_tenletter] = ten_value
                    s = "".join(s)
                    print(s)
                    s = list(s)
                    for i in range(len_tenletter - 1):
                        s[pos_tenletter + 1 + counter] = ""
                        counter = counter + 1
                    counter = 0
                    s[pos_singleletter] = sL2_value
                    for i in range(L_sL2 - 1):
                        s[pos_singleletter + 1 + counter] = ""
                        counter = counter + 1
                    s[pos_singleletter + 1] = ""
                    s = "".join(s)
                    print (s)
                    if s.find(tenletter) == -1:
                        return (s)
            if stest == sL3:
                if not s.find(sL3) == -1:
                    counter = 0
                    if s.find(tenletter) == -1:
                        return s
                    if s.find(sL3) == -1:
                        return s
                    s = list(s)
                    print (pos_tenletter)
                    s[pos_tenletter] = ten_value
                    s = "".join(s)
                    print(s)
                    s = list(s)
                    for i in range(len_tenletter - 1):
                        s[pos_tenletter + 1 + counter] = ""
                        counter = counter + 1
                    counter = 0
                    s[pos_singleletter] = sL3_value
                    for i in range(L_sL3 - 1):
                        s[pos_singleletter + 1 + counter] = ""
                        counter = counter + 1
                    s[pos_singleletter + 1] = ""
                    s = "".join(s)
                    print (s)
                    if s.find(tenletter) == -1:
                        return (s)


















        
   














en = (" en ")
en_value = ("1")
s = bytt(en, en_value, s)
to = (" to ")
to_value = ("2")
s = bytt(to, to_value, s)
tre = (" tre ")
tre_value = ("3")
s = bytt(tre, tre_value, s)
fire = (" fire ")
fire_value = ("4")
s = bytt(fire, fire_value, s)
fem = (" fem ")
fem_value = ("5")
s = bytt(fem, fem_value, s)
seks = (" seks ")
seks_value = ("6")
s = bytt(seks, seks_value, s)
syv = (" syv ")
syv_value = ("7")
s = bytt(syv, syv_value, s)
åtte = (" åtte ")
åtte_value = ("8")
s = bytt(åtte, åtte_value, s)
ni = (" ni ")
ni_value = ("9")
s = bytt(ni, ni_value, s)
ti = (" ti ")
ti_value = ("10")
s = bytt(ti, ti_value, s)
ellve = (" ellve ")
ellve_value = ("11")
s = bytt(ellve, ellve_value, s)
tolv = (" tolv ")
tolv_value = ("12")
s = bytt(tolv, tolv_value, s)
tretten = (" tretten ")
tretten_value = ("13")
s = bytt(tretten, tretten_value, s)
fjorten = (" fjorten ")
fjorten_value = ("14")
s = bytt(fjorten, fjorten_value, s)
femten = (" femten ")
femten_value = ("15")
s = bytt(femten, femten_value, s)
seksten = (" seksten ")
seksten_value = ("16")
s = bytt(seksten, seksten_value, s)
sytten = (" sytten ")
sytten_value = ("17")
s = bytt(sytten, sytten_value, s)
atten = (" atten ")
atten_value = ("18")
s = bytt(atten, atten_value, s)
nitten = (" nitten ")
nitten_value = ("19")
s = bytt(nitten, nitten_value, s)
tjue = (" tjue ")
tjue_value = ("20")
s = bytt(tjue, tjue_value, s)
tretti = (" tretti ")
tretti_value = ("30")
s = bytt(tretti, tretti_value, s)
førti = (" førti ")
førti_value = ("40")
s = bytt(førti, førti_value, s)
femti = (" femti ")
femti_value = ("50")
s = bytt(femti, femti_value, s)
seksti = (" seksti ")
seksti_value = ("60")
s = bytt(seksti, seksti_value, s)
sytti = (" sytti ")
sytti_value = ("70")
s = bytt(sytti, sytti_value, s)
åtti = (" åtti ")
åtti_value = ("80")
s = bytt(åtti, åtti_value, s)
nitti = (" nitti ")
nitti_value = ("90")
s = bytt(nitti,nitti_value, s)
hundre = (" hundre ")
hundre_value= ("100")
s = bytt(hundre, hundre_value, s)


tretti_ten = (" tretti")
tretti_ten_value = ("30")
s = tierbytt(tretti_ten, tretti_ten_value, s)


femti_ten = (" femti")
femti_ten_value = ("50")
       
s = tierbytt(femti_ten, femti_ten_value, s)



print (s)
lukk = input("Vil du lukke dette vinduet? ")  

    


