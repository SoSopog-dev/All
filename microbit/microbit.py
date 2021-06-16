from microbit import*
import randint


boat = Image("05050:05050:05050:99999:09990")

stein = Image(" 50005:05050:00500:05050:50005")

saks = Image(" 00000: 05050: 00500: 05050: 00000")

papir = Image(" 99999: 90009: 90009: 90009: 99999")


#main loop: This is where the main program runs
while True:
    usenumber = 0
    if button_a.is_pressed():
        userbutton = 1

    if button_b.is_pressed():
        userbutton = 2
    if userbutton == 1 and button_b.is_pressed():
        userbutton = 3

    number = randint(1,3)
    sleep(20)
    if number = 1:
        display.show(papir)
    if number = 2:
        dispaly.show(stein)
    if number = 3:
        display.show(saks)
    #makes the program sleep
