

jet = [[":", "@", ":"],
         ["(", "^", ")"],
         ["(", "^", ")"]]

vertical_beam=[["|"],
               ["|",],
               ["|",]]
            
horizontal_beam=["-","-","-","-"]

angled_beam=[[" ", " ", "/"],
            [" ", "/", " "],
            ["/", " ", " "]]

bullet= ["=",">"]

powerboost = [["*","*"], 
              ["*","*"]]

magnet =[["M", "M", "M"],
            ["M", "M", "M"],
            ["M", "M", "M"]]


dragon =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '`', ':', '.', '`', '-', '-', '-', '.', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '.', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', ':', '.', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', '(', ',', "'", ' ', ' ', ' ', ' ', ' ', '`', '/', ' ', ' ', ' ', '\\', '.', ' ', ' ', ' ', ',', '-', '-', '.', '_', '_', '_', '`', '.', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ',', ' ', ',', "'", ' ', ' ', ',', '-', '-', '.', ' ', ' ', '`', ',', ' ', ' ', ' ', '\\', '.', ';', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '`', '{', 'D', ',', ' ', '{', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ':', ' ', ' ', ' ', ' ', '\\', ';', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '`', '{', 'D', ',', ' ', '{', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ':', ' ', ' ', ' ', ' ', '\\', ';', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', 'j', ';', ';', ' ', ' ', ' ', ' ', '/', ' ', ' ', ',', "'", ' ', ',', '-', '/', '/', '.', ' ', ' ', ' ', ' ', ',', '-', '-', '-', '.', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' '],   
         [' ', ' ', '\\', ';', "'", ' ', ' ', ' ', '/', ' ', ' ', ',', "'", ' ', '/', ' ', ' ', '_', ' ', ' ', '\\', ' ', ' ', '/', ' ', ' ', '_', ' ', ' ', '\\', ' ', ' ', ' ', ',', "'", '/', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '`', "'", ' ', ' ', '/', ' ', '\\', ' ', ' ', '`', "'", ' ', ' ', '/', ' ', '\\', ' ', ' ', '`', '.', "'", ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', '_', '_', '_', ',', "'", ' ', ' ', ' ', '`', '.', '_', '_', ',', "'", ' ', ' ', ' ', '`', '.', '_', '_', ',', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

'''
    Getting input 
'''

'''
    UP : 0
    LEFT : 1
    RIGHT : 2
    QUIT : 3
'''

# key presses
UP, LEFT, RIGHT, QUIT,SHIELD, FIRE = range(6)
DIR = [UP, LEFT, RIGHT]
INVALID = -1

# allowed inputs
_allowed_inputs = {
    UP      : ['w', '\x1b[A'], \
    LEFT    : ['a', '\x1b[D'], \
    RIGHT   : ['d', '\x1b[C'], \
    QUIT    : ['q'], \
    SHIELD  : [' '], \
    FIRE    : ['b']
}

def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return INVALID

# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:

    def __init__(self):
        #try:
        #    self.impl = _GetchWindows()
        #except ImportError:
        self.impl = _GetchUnix()


    def __call__(self):
        return self.impl()


class _GetchUnix:


    def __init__(self):
        import tty, sys


    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

'''
class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        import msvcrt
        return msvcrt.getch()
'''

_getch = _Getch()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    #signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''             