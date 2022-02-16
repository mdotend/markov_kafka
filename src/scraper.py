import requests

def runScrape(pUrls):
    result = ""
    for url in pUrls:
        page = requests.get(url)
        result += page.content.decode("utf-8") 
        
    return result
