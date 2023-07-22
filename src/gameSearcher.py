# Description: This script will search for the best price of a game in different websites
# Author: @pablo-2k03 on @github
# Date: 21/07/2023
# Version: 1.1
# Any suggestions or improvements are welcome --> github.com/pablo-2k03


import requests
import re
import sys
sys.path.append("..")
from utils.helpers import *

pages = {
    "steam": "https://store.steampowered.com/search/?term=",
    "eneba": "https://www.eneba.com/es/marketplace?text=",
    "gog": "https://www.gog.com/en/game/",
}



class Scrappers:
    
    def __init__(self):
        pass
    
    def steamScrapper(self,game):

        game = game.replace(" ", "-")
        query = pages['steam']+game
        
        try:
            response = requests.get(query)
            page_html = response.text
            

            steam_price = re.findall('<div class="discount_final_price">\d{0,4},\d{0,3}€', page_html)[0]
            
            #Get only the price digits  
            steam_price = re.findall('\d{0,4},\d{0,3}', steam_price)[0]
            
            
            game = giveFormat(game)            
            return steam_price
        except:   
            return None


    


    def enebaScrapper(self,game):
        
        game = game.replace(" ", "-")
        game = game.lower()
        query = 'https://www.eneba.com/es/steam-'+game+'-steam-key-global'
        try:
            
            response = requests.get(query)
            if not check_availability(query):
                response = find_first_url_eneba(game)
                
            page_html = response.text
            
            eneba_prices = re.findall('\d{0,4},\d{0,3} €',page_html)
            
            #Remove xA0 (special character) from the price
            eneba_prices = [price.replace('\xa0', '') for price in eneba_prices]
            
            #Remove the € symbol
            eneba_prices = [price.replace('€', '') for price in eneba_prices]
                    
            best_price = eneba_prices[0]
            
            game = giveFormat(game)
            return best_price
            
        except:  
            return None


    def gog_Scrapper(self,game):
        
        game = game.replace(" ", "_")
        game = game.lower()
        query = pages['gog']+game
        
        try:
            
            response = requests.get(query)
            page_html = response.text
            
            pattern = r'"finalAmount":"(\d+\.\d+)"'
            prices = re.findall(pattern, page_html)
            if prices == []:
                return None
            best_price = prices[0]
            
            game = giveFormat(game)
            game = game.replace("_", " ")
            
            return best_price
            
        except:
            return None
        
