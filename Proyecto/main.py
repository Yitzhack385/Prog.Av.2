

from Menu.menu import Menu
from ZOO.zoo import Zoo

def main():
    zoo = Zoo()
    menu = Menu(zoo)
    try:
        menu.login()
    except Exception as e:
        print(f"Error durante la ejecución del programa: {e}")

if __name__ == "__main__":
    main()