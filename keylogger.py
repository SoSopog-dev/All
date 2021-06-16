import keyboard
import time
content = ""
def callback(event):
    keypress = event.name
    type = event.type
    print(type)
    time.sleep(1000)
    if type == "DOWN_PRESS":
        wait = False
    

def main():
    run = True
    modus = 0
    while run:
        k = keyboard.read_key()
        if k == "space":
            k = ""
        print(k)
        r = open("presses.txt", "r")|
        content = r.read()
        r.close() 
        f = open("presses.txt", "w")
        f.write(content + k) 
        f.close()
        wait = True
        while wait:
            keyboard.on_release(callback = callback)
        if k == "p":
            keyboard.write(content)



if __name__ == "__main__":
    main()



