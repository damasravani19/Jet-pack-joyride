import objects
import numpy as np
from globalvariables import globalvariables
from random import randint
class people:
    def __init__(self):
        self._construct()
        self._lenght=3
        self._width=3
        self._posy=4
        self._posx=28
        self._bullets=[]

    def _checkcoins(self,board,globalvariables):
        for i in range(self._posx,self._posx+3):
            for j in range(self._posy+3):
                if board._display[i][j]=="$":
                    board._matrix[i][j+globalvariables._getk()]=" "
                    globalvariables._increasescore()

    def _checkbeam(self,board,globalvariables):
        flag=0
        for i in range(self._posx,self._posx+3):
            for j in range(self._posy,self._posy+3):
                if (board._display[i][j]=="-"or board._display[i][j]=="|"):
                    flag=1
                elif board._display[i][j]=="/":
                    flag=1
        
        if flag==1:
            if (globalvariables._getinshield()==0):
                globalvariables._decreaselives()


    def _checkpowerboost(self,board,globalvariables):
        print("cccccccccccccccccccccppppppppppppppppppppppppppppppp")
        flag=0
        for i in range(self._posx,self._posx+3):
            for j in range(self._posy,self._posy+3):
                if board._display[i][j]=="*":
                    flag=1
                    for m in range(i-1,i+2):
                        for n in range(j-1,j+2):
                            board._matrix[m][n+globalvariables._getk()]=" "
                    globalvariables._increasea()
                    break
            if flag==1 :
                break

    def _checkmagnet(self,board,globalvariables):
        print("innnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        #initial check if jetpack is touching the magnet
        x=0
        for i in range(self._posx,self._posx+3):
            for j in range(self._posy,self._posy+3):
                if board._display[i][j]=="M":
                    print("checkbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                    x=1
                    self._posy=self._posy-(3-(j-self._posy))
                    break
                if x==1:
                    break

        flag1=0
        # for i in range(0,34):
        for j in range(self._posy+3,self._posy+18):
            for i in range(0,34):
                if board._display[i][j]=="M":
                    print("outtttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")
                    self._posy=self._posy+3
                    flag1=1
                    break
            if flag1==1 :
                break

        # after attraction from the magnet checking if he is colliding with the magnet
        # if flag1==1:
        #     y=0
        #     for i in range(self._posx,self._posx+3):
        #         for j in range(self._posy,self._posy):
        #             if board._display[i][j]=="M":  
        #                 print("checkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        #                 y=1
        #                 self._posy=self._posy-(3-(j-self._posy))
        #                 break
        #         if y==1:
        #             break

        flag2=0
        for i in range(self._posx,self._posx+3):
            for j in range(self._posy,self._posy-6):
                if board._display[i][j]=="M":
                    print("innnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                    self._posy=self._posy-2
                    flag2=1
                    break
            if flag2==1 :
                break

    def _check(self,board,globalvariables):
        self._checkcoins(board,globalvariables)  
        self._checkbeam(board,globalvariables)
        self._checkpowerboost(board,globalvariables)
        self._checkmagnet(board,globalvariables)

    def _construct(self):
        self._arr1=objects.jet

    def print(self,board,bosenemy,globalvariables):
        print("jppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
        for i in range(3):
            for j in range(3):
                board._display[self._posx+i][self._posy+j]=self._arr1[i][j]
        print(globalvariables._getk())
        if globalvariables._getk()==1300:
            bosenemy._bossprint(board)
    
    def move_right(self,board,globalvariables):
        if (globalvariables._getk==1300):
            if self._posy+3<=100:
                self._posy=self._posy+3
        else :
            if self._posy+3<=145:
                self._posy=self._posy+3

        self._check(board,globalvariables)
        
    def move_left(self,board,globalvariables):
        if self._posy-3>=0:
            self._posy=self._posy-3
        self._check(board,globalvariables)

    def move_up(self,board,globalvariables,bosenenemy):
        if self._posx-3>=2:
            self._posx=self._posx-3
        self._check(board,globalvariables)
        if(globalvariables._getk()==1300):
            bosenenemy._move_up()

    def check_bullets(self,board,x,y,globalvariables,bosenemy,bulletno):
        #checking for horizontal beams
        if (board._display[x][y+1]=="-"):
            # arr1=np.empty([1,4],dtype=object)
            if(board._display[x][y]=="-"):
                board._matrix[x][y+globalvariables._getk()]=" "
                board._matrix[x][y+globalvariables._getk()+1]=" "
                board._matrix[x][y+globalvariables._getk()+2]=" "
                board._matrix[x][y+globalvariables._getk()-1]=" "
                board._matrix[x][y+globalvariables._getk()+3]=" "
                # board._matrix[x][y-1+globalvariables._getk():y+3+globalvariables._getk()]=arr1
            elif(board._display[x][y]!="-"):
                board._matrix[x][y+globalvariables._getk()+4]=" "
                board._matrix[x][y+globalvariables._getk()+1]=" "
                board._matrix[x][y+globalvariables._getk()+2]=" "
                board._matrix[x][y+globalvariables._getk()+3]=" "
                # board._matrix[x][y+globalvariables._getk():y+4+globalvariables._getk()]=arr1 

          #checking for vertical beams      
        elif (board._display[x][y]=="|"):
            if board._display[x+1][y]=="|" and board._display[x-1][y]!="|":
                board._matrix[x][y+globalvariables._getk()]=" "
                board._matrix[x+1][y+globalvariables._getk()]=" "
                board._matrix[x+2][y+globalvariables._getk()]=" "
            elif board._display[x+1][y]=="|" and board._display[x-1][y]=="|":
                board._matrix[x][y+globalvariables._getk()]=" "
                board._matrix[x+1][y+globalvariables._getk()]=" "
                board._matrix[x-1][y+globalvariables._getk()]=" "
            elif board._display[x-1][y]=="|" and board._display[x+1][y]!="|":
                board._matrix[x][y+globalvariables._getk()]=" "
                board._matrix[x-2][y+globalvariables._getk()]=" "
                board._matrix[x-1][y+globalvariables._getk()]=" "
          #checking for angled beams
        elif(board._display[x][y-1]=="/"): 
            print("innnnnnnnnnnnnnnnnnnnnnnnnn")
            if(board._display[x+1][y-2]=="/" and board._display[x-1][y]!="/"):
                print("11111111111111111")
                board._matrix[x][y+1+globalvariables._getk()]=" "
                board._matrix[x+1][y+globalvariables._getk()]=" "
                board._matrix[x+2][y-1+globalvariables._getk()]=" "
            elif(board._display[x+1][y-2]=="/" and board._display[x-1][y]=="/"):
                print("222222222222222222222")
                board._matrix[x+1][y+globalvariables._getk()]=" "
                board._matrix[x-1][y+2+globalvariables._getk()]=" "
                board._matrix[x][y+1+globalvariables._getk()]=" "
            elif(board._display[x+1][y-2]!="/" and board._display[x-1][y]=="/"):
                print("333333333333333333333")
                board._matrix[x][y+1+globalvariables._getk()]=" "
                board._matrix[x-1][y+2+globalvariables._getk()]=" "
                board._matrix[x-2][y+3+globalvariables._getk()]=" "

        if globalvariables._getk()==1300:
            bosenemy._checkbullet(x,y+1,board,globalvariables,bulletno)

        if (board._display[x][y]=="E"):
            globalvariables._increasescore()
            board._matrix[x][y+globalvariables._getk()]=" "
            board._matrix[x+1][y+globalvariables._getk()]=" "   

    def firebullet(self):
        temp=[]
        temp.extend([self._posx+1,self._posy+3])
        self._bullets.append(temp)
        # print(self._bullets)

    def move_bullets(self,board,globalvariables,bosenemy):
        for i in range(0,len(self._bullets)-1):
            if ((self._bullets[i][1])+1)<=146:
                self._bullets[i][1]=self._bullets[i][1]+1
                # print(self._bullets[i][0],self._bullets[i][1])
                self.check_bullets(board,self._bullets[i][0],self._bullets[i][1],globalvariables,bosenemy,i)
                # self._bullets[i][1]=self._bullets[i][1]+2
                # board._matrix[self._bullets[i][0]][self._bullets[i][1]+globalvariables._getk()]="="
                # board._matrix[self._bullets[i][0]][self._bullets[i][1]+1+globalvariables._getk()]=">"
                # board._matrix[self._bullets[i][0]][self._bullets[i][1]-2+globalvariables._getk()]=" "
                # board._matrix[self._bullets[i][0]][self._bullets[i][1]-3+globalvariables._getk()]=" "
                board._display[self._bullets[i][0]][self._bullets[i][1]]=">"
                # board._display[self._bullets[i][0]][self._bullets[i][1]+1]=">"
            # self.check_bullets(board,self._bullets[i][0],self._bullets[i][1],globalvariables)

    def gravity(self,bosenenemy,globalvariables):
        if self._posx<28 and self._posx+1<=28:
            self._posx=self._posx+1
            if(globalvariables._getk()==1300):
                bosenenemy._bossmovedown()

        
class bossenemy(people):

    def __init__(self):
        self._posx=19
        self._posy=100
        self._construct()
        self._iceballs=[]
        self._bullethit=[]

    def _construct(self):
        self._arr2=objects.dragon

    def _throwiceball(self):
        temp=[]
        temp.extend([self._posx+1,self._posy-1])
        self._iceballs.append(temp)

    def _moveiceballs(self,jet,board,globalvariables):
        if(globalvariables._getk()==1300):
            for i in range(0,len(self._iceballs)-1):
                flag=0
                for m in range(jet._posx,jet._posx+3):
                    for n in range(jet._posy,jet._posy+3):
                        if m==self._iceballs[i][0] and n==self._iceballs[i][1]:
                            globalvariables._decreaselives()
                            flag=1
                            break
                    if flag==1:
                        break
                if flag==0:
                    if self._iceballs[i][1]-2>=0 :
                        self._iceballs[i][1]=self._iceballs[i][1]-2
                        board._display[self._iceballs[i][0]][self._iceballs[i][1]]="#"
  #check for jetpack position here if the snowball collides =>> done

    def _move_up(self):
        if self._posx-3>=2:
            self._posx=self._posx-3
        self._throwiceball()

        #check if any bullet is collide with the dragon

    def _bossmovedown(self):
        if self._posx<19 and self._posx+1<=19:
            self._posx=self._posx+1

        #check if the bullet collide swith the dragon

    def _bossprint(self,board):
        for i in range(0,12):
            for  j in range(0,42):
                board._display[self._posx+i][self._posy+j]=self._arr2[i][j]

    def _checkbullet(self,x,y,board,globalvariables,bulletnum):
        flag1=0
        for i in range(0,len(self._bullethit)-1):
            if self._bullethit[i]==bulletnum:
                flag1=1
        if flag1==0:
            flag=0
            for i in range(self._posx,self._posx+12):
                for  j in range(self._posy,self._posy+142):
                    if (i==x and j==y):
                        if (board._display[i][j]!=" "):
                            self._bullethit.append(bulletnum)
                            globalvariables._decreasedragonlives()
                            flag=1
                            break
                if flag==1:
                    break


class enemy(people):
    def __init__(self,board):
        self.__character="-"
        self.__x=29
        self.__y=randint(30,1300)
        self._placeenemy(board)

    def _placeenemy(self,board):
        board._matrix[self.__x][self.__y]="E"
        board._matrix[self.__x+1][self.__y]="E"
                        

                


         
        


