#!usr/bin/python3
import os
import numpy as np
import time
import objects
from random import randint
from datetime import datetime
from coins import coins
from verticalbeams import verticalbeams
from horizontalbeams import horizontalbeams
from angledbeams import angledbeams
from people import enemy
class board:
    def __init__(self):
        self._matrix = np.empty([35,1550],dtype=object)
        self._display = np.empty([35,1500],dtype=object)
        self._display[:]=' '
        self._matrix[:]=' '
        self._coinslocation=list()
        self._vbeamlocation=list()

    def _setmatrixvalue(self,m,n,value):
        self._matrix[m][n]=value
    def _getmatrixvalue(self,m,n):
        return self._matrix[m][n]
    def _createboard(self,board):
        self._coinsdeclare(board)
        self.sky()
        self.ground()
        self.beams(board)
        self.powerboost()
        self.magnet()
        self.enemy(board)
        # self.benemy()
    def _coinsdeclare(self,board) :
        for i in range(50):
            a=coins(board)
    def verticalbeams(self,board):
        for i in range(20):
            a=verticalbeams(board)
            
    def horizontalbeams(self,board):
        for i in range(20):
            a=horizontalbeams(board)

    def angledbeams(self,board):
        for i in range(20):
            a=angledbeams(board)
            
    def powerboost(self):
        for i in range(10):
            x=randint(2,25)
            y=randint(10,1340)
            flag=0
            for j in range(x-1,x+3):
                for k in range(y-1,y+3):
                    if self._matrix[j][k]=="$" or self._matrix[j][k]=="|" or self._matrix[j][k]=="-" or self._matrix[j][k]=="/":
                        flag=1

            arr5=np.empty([2,2],dtype=object)
            if flag==0:
                arr5=objects.powerboost
                self._matrix[x:x+2,y:y+2]=arr5

    def magnet(self):
        for i in range(20):
            x=randint(2,25)
            y=randint(10,1300)
            flag=0
            for j in range(x-3,x+6):
                for k in range(y-3,y+6):
                    if self._matrix[j][k]=="$" or self._matrix[j][k]=="|" or self._matrix[j][k]=="-" or self._matrix[j][k]=="/" or self._matrix[j][k]=="*":
                        flag=1
            arr6=np.empty([3,3],dtype=object)
            if flag==0:
                arr6=objects.magnet
                self._matrix[x:x+3,y:y+3]=arr6

    def beams(self,board):
        self.verticalbeams(board)
        self.horizontalbeams(board)
        self.angledbeams(board)
    def sky(self):
        for i in range(1499):
            self._matrix[0][i]='"'
            self._matrix[1][i]='"'
    def ground(self):
        for i in range(1499):
            self._matrix[34][i]='-'
            self._matrix[33][i]='-'
            self._matrix[32][i]='-'
            self._matrix[31][i]='-'

    def enemy(self,board):
        for i in range(20):
            z=enemy(board)


  