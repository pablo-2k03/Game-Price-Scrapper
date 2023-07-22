from src.gameSearcher import Scrappers
from utils.helpers import *
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama to automatically reset colors

def main():
    searchers = Scrappers()
    
    game = input('Enter the game you want to search: ')
    
    game = game.replace("'","")
    
    steam_price = searchers.steamScrapper(game)
    eneba_price = searchers.enebaScrapper(game)
    gog_price = searchers.gog_Scrapper(game)
    
    
    prices = {
              "steam": steam_price,
              "eneba": eneba_price,
              "gog": gog_price
             }
    
    for i in prices:
        if prices[i] is None:
            print(f"{Fore.LIGHTRED_EX}[-] {i.title()} price for {game}: Not found")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[+] {i.title()} price for {game}: {prices[i]}€")
    
    
    
if __name__ == "__main__":
    main()