#vær program
import os
def main():
    run = True
    day = 0
    days = ["Mandag", "Tirstag", "Onsdag", "Torstag", "Fredag", "Lørdag", "Søndag"]
    path = os.getcwd()
    filename = "temp.txt"
    dir = os.listdir(path)
    if not filename in dir:
        f = open(filename, "w")
        f.write("Weather file \n")
        f.close()
    def data():
        f = open(filename, "r")
        content = f.read()
        f.close()
        print (content)
    print("\n What do you want to do? print earlier content or write in more data ")
    command = input("p/w :")
    if command == "p":
        data()
    elif command == "w":
        week = input("\n Week:")
        f = open(filename, "r")
        content = f.read()
        f.close()
        f = open(filename, "w")
        f.write(content + "\n"+ "Week: " + week +"\n")
        f.close()
        while run:
            print("\n " ,days[day] )
            temp = input("\n Tempratur:")
            vind = input("\n Wind:")
            regn = input("\n Rain:")
            ok = input("\n All ok:")
            if temp != "No" and vind != "No" and regn != "No" and ok != "No":
                f = open(filename, "r")
                content = f.read()
                f.close()
                f = open(filename, "w")
                f.write(content)
                temp = "temperature: " + temp + "° celsius"
                vind = "wind speed: " + vind + " m/s"
                regn = "rain amount: " + regn + " mm"
                data = days[day] + "\n" + temp + "\n"+ vind  + "\n"+ regn + "\n" 
                f.write(data)
                f.close()
                if day == 6:
                    day = 0
                    run = False
                else:
                    day += 1
    else:
        print("not a valid response")
if __name__ == "__main__":
    main()