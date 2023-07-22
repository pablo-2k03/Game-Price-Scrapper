import requests
import re
from colorama import init, Fore, Style

init(autoreset=True)  #Reset the colors after each print

def quitSpace(string):
    string = string.replace("-", " ")
    return string

def check_availability(query):
    
    response = requests.get(query)
    regex_to_find = '<strong>Lo sentimos, agotado'
    
    if response.status_code == 200:
        if re.search(regex_to_find, response.text):
            return False
        return response
    
    else:
        return False
    
    
def giveFormat(game):
    game = quitSpace(game)
    game = game.title()
    return game


def find_first_url_eneba(game):
    url_to_try = {
        "rockstar_key": "https://www.eneba.com/es/rockstar-social-club-"+game+"-premium-online-edition-rockstar-games-launcher-key-europe",
        "remakes": "https://www.eneba.com/es/steam-"+game+"-remake-steam-key-global",
        "pc_global": "https://www.eneba.com/es/steam-"+game+"-pc-steam-key-global",
        "pc_europe": "https://www.eneba.com/es/steam-"+game+"-pc-steam-key-europe", 
        "key_europe": "https://www.eneba.com/es/steam-"+game+"-steam-key-global",
        "gog_key": "https://www.eneba.com/es/gog-"+game+"-gog-com-key",
        "others": "https://www.eneba.com/es/other-"+game+"-pc-official-website-key-europe"
    }
    
    for value in url_to_try.values():
        
        sol = check_availability(value)
        
        if sol != False:
            return sol
        

def view_prices(prices,game):
    
    for i in prices:
        if prices[i] is None:
            print(f"{Fore.LIGHTRED_EX}[-] {i.title()} price for {game}: Not found")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[+] {i.title()} price for {game}: {prices[i]}€")
    