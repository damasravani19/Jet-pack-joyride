
class globalvariables:
    def __init__(self):
        self.__k=0
        self.__coins=0
        self.__lives=5
        self.__a=100
        self.__score=0
        self._initialtime=300
        self._timeremaining=300
        self.__shieldactive=1 # variable which shows whether shield can be activated or not
        self.__inshield=0     # whether jetpack in on shield or not 
        self.__dragonlives=2
    
    def _incrementk(self):
        self.__k=self.__k+self._a

    def _getk(self):
        return self.__k
    def _decreaselives(self):
        self._lives=self._lives-1

    def _increasea(self):
        self._a=self._a+1

    def _getshieldactive(self):
        return self._shieldactive
  
    def _getinshield(self):
        return self._inshield
        
    def _getintoshield(self):
        self._inshield=1
        self._shieldactive=0

    def _getoffshield(self):
        self._inshield=0

    def _activateshieldactive(self):
        self._shieldactive=1
    
    def _increasescore(self):
        self._score=self._score+10
    
    def _calremainingtime(self,i):
        self._timeremaining=self._initialtime-i

    def _decreasedragonlives(self):
        self._dragonlives=self._dragonlives-1

    def _check(self):
        if self._lives==0:
            print("YOU LOST THE GAME :((( NO LIVES ")
            quit()
        elif self._dragonlives==0:
            print("YOU WON THE GAME!!!! YAYYYYYYY!!!!")
            quit()
        elif self._timeremaining==0:
            print("NO TIME REAMAINING!!! :(((")

    def _printvariables(self):
        print("no of lives remaining ",self._lives)
        print("score ",self._score)
        print("remaining time",self._timeremaining)
        print("can shield be activated",self._shieldactive)
        print("inshield",self._inshield)
        print("remaining lives of the",self._dragonlives)
        print("printing the value of a ",self._a)

    