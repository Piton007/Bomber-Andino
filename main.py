from cli import change_console_color,print_banner
from api import Api,Attacker
from menu import Menu

def setup():
    api = Api()
    return Attacker(api)

if __name__ == "__main__":

    print_banner()
    menu = Menu()
    answers = menu.answers()
    change_console_color()
    attacker = setup()
    attacker.attack(answers['phone_number'],answers['country_code'],answers['custom_msg'],int(answers['quantity']))
  

