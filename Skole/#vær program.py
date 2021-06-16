#vær program
import os

def main():
    run = True
    day = 0
    days = ["Mandag", "Tirstag", "Onsdag", "Torstag", "Fredag", "Lørdag", "Søndag"]
    path = os.getcwd()
    filename = "temp.txt"
    file = os.path.join(filename, path)
    dir = os.listdir(path)
    if not "temp.txt" in dir:
        f = open(file, "w")
        f.write("Weather file \n")
        f.close()
    while run:
        print("\n " ,days[day] )
        temp = input("\n Tempratur:")
        vind = input("\n Vind:")
        regn = input("\n Regn:")

        if not temp == "Feil" or vind == "Feil" or regn == "Feil":
            f = open(file, "r")
            content = f.read()
            f.close()
            f = open(file, "w")
            
            f.write(content,"\n", days[day], "\n", temp, "\n", vind, "\n", regn)
            f.close()
        if day == 7:
            day = 0
            run = False
        else:
            day += 1

            



if __name__ == "__main__":
    main()