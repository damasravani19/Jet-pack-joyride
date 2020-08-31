from random import randint
import numpy as np
import objects

class angledbeams:
    def __init__(self,board):
        self.__character="-"
        self.__x=randint(2,25)
        self.__y=randint(10,1300)
        self._placeangledbeam(board)

    def _placeangledbeam(self,board):
        flag=0
        for j in range(self.__x,self.__x+3):
            for k in range(self.__y,self.__y+3):
                if board._matrix[j][k]=="$" or board._matrix[j][k]=="|" or board._matrix[j][k]=="-":
                    flag=1
        arr4=np.empty([3,3],dtype=object)
        if flag==0:
            arr4=objects.angled_beam
            board._matrix[self.__x:self.__x+3,self.__y:self.__y+3]=arr4
        