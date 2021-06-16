a = input()
s = list(a)
s = "".join(s)

def bytt(letter, letter_value, s):
    for i in range(len(a)):
        len_letter = (len(letter)) -1
        if not s.find(letter)== -1:
            pos_letter = s.find(letter)
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
        print(s)
       
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

hundre = (" hundre ")
hundre_value= ("100")
s = bytt(hundre, hundre_value, s)

print (s)
