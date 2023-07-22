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
    
    view_prices(prices,game)
    
    
    
if __name__ == "__main__":
    main()