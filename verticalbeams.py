from random import randint
import numpy as np
import objects

class verticalbeams:
    def __init__(self,board):
        self.__character="|"
        self.__x=randint(2,27)
        self.__y=randint(0,1300)
        self._placeverticalbeam(board)

    def _placeverticalbeam(self,board):
        flag=0
        for j in range(self.__x,self.__x+3):
            if board._matrix[j][self.__y]=="$":
                    flag=1
        arr2=np.empty([3,1],dtype=object)
        if flag==0 :
            arr2=objects.vertical_beam
            board._matrix[self.__x:self.__x+3,self.__y:self.__y+1]=arr2
