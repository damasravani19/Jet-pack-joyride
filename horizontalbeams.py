from random import randint
import numpy as np
import objects

class horizontalbeams:
    def __init__(self,board):
        self.__character="-"
        self.__x=randint(2,29)
        self.__y=randint(10,1300)
        self._placehorizontalbeam(board)

    def _placehorizontalbeam(self,board):
        flag=0
        for j in range(self.__y,self.__y+4):
            if board._matrix[self.__x][j]=="$" or board._matrix[self.__x][j]=="|":
                flag=1
        arr3=np.empty([1,4],dtype=object)
        if flag==0:
            arr3=objects.horizontal_beam
            board._matrix[self.__x:self.__x+1,self.__y:self.__y+4]=arr3