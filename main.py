#!usr/bin/python3
 
from background import board
from people import people 
from people import bossenemy
from globalvariables import globalvariables
from colorama import init,Fore, Back, Style 
import objects
import os
import time
init()
# from people import people/
x=board()
x._createboard(x)
gvariables=globalvariables()
benemy=bossenemy()
#x.print()

jetpack=people()
now=time.time()
shieldtimestart=int(time.time())-20
while True:
    later=time.time()
    diff=int(later-now)
    if(int(later-shieldtimestart)==10):
        gvariables._getoffshield()
    if(int(later-shieldtimestart)==70):
        gvariables._activateshieldactive()
    gvariables._calremainingtime(diff)
    # PRINTING
    jetpack._check(x,gvariables)
    for i in range(35):
        for j in range(gvariables._getk(),gvariables._getk()+148):
            x._display[i][j-gvariables._getk()]=x._getmatrixvalue(i,j)
    event = objects.get_key(objects.get_input())

    if event == objects.QUIT:
        # global_funct.display_ending("YOU QUITTER!")
        break
    
    elif event == objects.LEFT:
        jetpack.move_left(x,gvariables)

    elif event == objects.RIGHT:
        jetpack.move_right(x,gvariables)

    elif event == objects.UP:
        jetpack.move_up(x,gvariables,benemy)

    elif event == objects.FIRE:
        jetpack.firebullet()

    elif event == objects.SHIELD:
        if (gvariables._getshieldactive()):
            gvariables._getintoshield()
            shieldtimestart=time.time()
    jetpack.gravity(benemy,gvariables)
    jetpack.print(x,benemy,gvariables)
    jetpack._check(x,gvariables)
    jetpack.move_bullets(x,gvariables,benemy)
    benemy._moveiceballs(jetpack,x,gvariables)
    os.system('clear')
    for i in range(35):
        for j in range(gvariables._getk(),gvariables._getk()+148):
            if x._display[i][j-gvariables._getk()]=="$":
                print(Fore.YELLOW + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="M":
                print(Fore.RED + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="*":
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="\"":
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="@" and gvariables._getinshield():
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="^" and gvariables._getinshield():
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]=="(" and gvariables._getinshield():
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]==")" and gvariables._getinshield():
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            elif x._display[i][j-gvariables._getk()]==":" and gvariables._getinshield():
                print(Fore.BLUE + x._display[i][j-gvariables._getk()],end='')
            else :
                print(Fore.WHITE + x._display[i][j-gvariables._getk()],end='')
        print()

    # for m in range(jetpack._posx,jetpack._posx+3):
    #     for n in range(jetpack._posy,jetpack._posy+3):
    #         if(gvariables._inshield):
    #             print(Fore.BLUE + x._display[i][j],end='')
    #         else :
    #             print(Fore.WHITE + x._display[i][j],end='')

    gvariables._printvariables()
    gvariables._check()
    time.sleep(0.2)
    if gvariables._getk()<1300:
        gvariables._incrementk()
