from random import randint

class coins:
    def __init__(self,board):
        self.__character="$"
        self.__x=randint(2,27)
        self.__y=randint(0,1300)
        self._placecoin(board)

    def _placecoin(self,board):
        board._matrix[self.__x][self.__y]="$"
        board._matrix[self.__x][self.__y+1]="$"
        board._matrix[self.__x+1][self.__y]="$"
        board._matrix[self.__x+1][self.__y+1]="$"


            