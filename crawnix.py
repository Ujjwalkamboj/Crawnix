import win_unicode_console , colorama
import os , subprocess

width = os.get_terminal_size().columns

# Windows deserves coloring too :D
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\33[97m'  # white

def banner():
    print("""%s
                _________                              _________  __
                __  ____/____________ ___      ___________(_)_  |/ /
                _  /    __  ___/  __ `/_ | /| / /_  __ \_  /__    / 
                / /___  _  /   / /_/ /__ |/ |/ /_  / / /  / _    |  
                \____/  /_/    \__,_/ ____/|__/ /_/ /_//_/  /_/|_|  %sv1.0\n""" % (W,R))



def directory():
    if os.path.isdir('directory'):
        pass
    else:
        os.mkdir('directory')

def crawl():
    from modules import crawler

#The main routine
def main():
    subprocess.call('clear')
    banner()
    a = 1
    if a == a:
        directory()
        crawl()

try:
    main()
except Exception as e:
    print("%s[-] No Internet Connection!"%(R))
