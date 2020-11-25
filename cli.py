from pyfiglet import Figlet
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
import time
import sys

APP_NAME = "BOMBER ANDINO"
FONT = "slant"

color = "\033[1;33m"

def change_console_color():
    sys.stdout.write(color)

def print_single_line(msg):
    sys.stdout.flush()
    sys.stdout.write("\r"+msg)

def custom_print(msg):
    cprint(msg,'yellow')

def print_banner():
    init(strip=not sys.stdout.isatty())
    cprint(figlet_format(APP_NAME, font=FONT),'yellow')
if __name__ == "__main__":
    print_banner()
    sys.stdout.write(color)
    cprint(figlet_format(APP_NAME, font=FONT),'red')