# Description: This script will search for the best price of a game in different websites
# Author: @pablo-2k03 on @github
# Date: 21/07/2023
# Version: 1.1
# Any suggestions or improvements are welcome --> github.com/pablo-2k03


import requests
import re

pages = {
    "steam": "https://store.steampowered.com/search/?term=",
    "eneba": "https://www.eneba.com/es/marketplace?text=",
    "gog": "https://www.gog.com/en/game/",
}


def quitSpace(string):
    string = string.replace("-", " ")
    return string

def steamScrapper(game):

    game = game.replace(" ", "-")
    query = pages['steam']+game
    
    try:
        response = requests.get(query)
        page_html = response.text
        

        steam_price = re.findall('<div class="discount_final_price">\d{0,4},\d{0,3}€', page_html)[0]
        
        #Get only the numbers  
        steam_price = re.findall('\d{0,4},\d{0,3}', steam_price)[0]
        
        
        game = quitSpace(game)
        print('[+] Steam Price for '+game+': '+steam_price+'€')
        
    except:
        
        game = quitSpace(game)
        print('[-] Steam Price for '+game+': Not found')



def check_availability(query):
    
    response = requests.get(query)
    regex_to_find = '<strong>Lo sentimos, agotado'
    
    if response.status_code == 200:
        if re.search(regex_to_find, response.text):
            return False
        return response
    
    else:
        return False


def find_first_url_eneba(game):
    url_to_trie = {
    
        "key_europe": "https://www.eneba.com/es/steam-"+game+"-steam-key-europe",
        "gog_key": "https://www.eneba.com/es/gog-"+game+"-gog-com-key",
        
    }
    
    for value in url_to_trie.values():
        
        sol = check_availability(value)
        
        if sol != False:
            return sol
        

def enebaScrapper(game):
    
    game = game.replace(" ", "-")
    game = game.lower()
    query = 'https://www.eneba.com/es/steam-'+game+'-steam-key-global'
    try:
        response = requests.get(query)
        if check_availability(query) == False:
            #print('[-] Eneba steam global key for '+game+': Not found')
            #print('[-] Searching others...')
            response = find_first_url_eneba(game)
        page_html = response.text
        
        eneba_prices = re.findall('\d{0,4},\d{0,3} €',page_html)
        #Remove xA0 from the price
        
        eneba_prices = [price.replace('\xa0', '') for price in eneba_prices]
        
        #Remove the € symbol
        eneba_prices = [price.replace('€', '') for price in eneba_prices]
                
        best_price = eneba_prices[0]
        
        
        game = quitSpace(game)
        game = game.title()
        print('[+] Eneba Price for '+game+': '+best_price+'€')
    except:
            
            game = quitSpace(game)
            game = game.title()
            print('[-] Eneba Price for '+game+': Not found')


def gog_Scrapper(game):
    
    game = game.replace(" ", "_")
    game = game.lower()
    query = pages['gog']+game
    
    try:
        
        response = requests.get(query)
        page_html = response.text
        
        pattern = r'"finalAmount":"(\d+\.\d+)"'
        prices = re.findall(pattern, page_html)
        if prices == []:
            raise Exception(print('[-] GOG Price for '+game+': Not found'))
        best_price = prices[0]
        
        game = quitSpace(game)
        game = game.title()
        game = game.replace("_", " ")
        print('[+] GOG Price for '+game+': '+best_price+'€')
        
    except Exception as e:
        pass
    

def gameSearcher():
    game = input('Enter the game you want to search: ')
    
    #Search for apostrophes and replace them with nothing
    game = game.replace("'", "")
    
    steamScrapper(game)
    enebaScrapper(game)
    gog_Scrapper(game)
   
if __name__ == '__main__':
    gameSearcher()

