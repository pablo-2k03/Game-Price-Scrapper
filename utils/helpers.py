import requests
import re


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
    url_to_trie = {
    
        "key_europe": "https://www.eneba.com/es/steam-"+game+"-steam-key-europe",
        "gog_key": "https://www.eneba.com/es/gog-"+game+"-gog-com-key",
        
    }
    
    for value in url_to_trie.values():
        
        sol = check_availability(value)
        
        if sol != False:
            return sol