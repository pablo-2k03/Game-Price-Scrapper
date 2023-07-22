from src.gameSearcher import Scrappers
from utils.helpers import *



def main():
    searchers = Scrappers()
    
    game = input('Enter the game you want to search: ')
    
    steam_price = searchers.steamScrapper(game)
    eneba_price = searchers.enebaScrapper(game)
    gog_price = searchers.gog_Scrapper(game)
    
    
    prices = {
              "steam": steam_price,
              "eneba": eneba_price,
              "gog": gog_price
             }
    
    for i in prices:
        if prices[i] == None:
            print('[-] '+i.title()+' price for '+game+': '+'Not found')
        else:
            print('[+] '+i.title()+' price for '+game+': '+prices[i]+'€')
    
    
    
if __name__ == "__main__":
    main()