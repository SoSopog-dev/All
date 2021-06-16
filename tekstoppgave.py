a = input()
s = list(a)



en = ("en")
len_en = (len(en))
def bytt(letter, len_letter, lettervalue):
    s = list(a)
    s = "".join(s)
    for i in range(len(a)):
        if s.find(letter):
            pos_letter = s.find(letter)
            print(pos_letter)
            if s.find(letter) == -1:
                break
            counter = 0
            s = list(s)
            s[pos_letter] = lettervalue
            for i in range(len_letter - 1):
                s[pos_letter + 1 + counter] = ""
                counter = counter + 1
            s = "".join(s)
            print(s)





to = ("to")
len_to = (len(to))
to_tall = ("2")
bytt(to,len_to, to_tall)
print(s)
    
    
