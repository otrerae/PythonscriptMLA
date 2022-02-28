import requests
import json
import sys

site_ID = sys.argv[1]
seller_IDs = sys.argv[2]

def seller_requestsAPI(site_ID, seller_ID):
    response = requests.get('https://api.mercadolibre.com/sites/'+site_ID+'/search?seller_id='+seller_ID)
    response_json = response.json()
    return response_json["results"]

def category_requestsAPI(category_ID):
    response = requests.get('https://api.mercadolibre.com/categories/'+category_ID)
    response_json = response.json()
    return response_json["name"]


def writeLog(site_ID, seller_ID):
    sellers = seller_ID.split(",")

    for seller in sellers:
        items = seller_requestsAPI(site_ID, seller)
        data = ''
        for item in items:
            category_Id = item["category_id"]
            category_name = category_requestsAPI(category_Id)
            
            text = 'ID: '+item["id"]+' Titulo: '+item["title"]+' Categoria: '+ category_name+' Categoria_ID: '+category_Id+'\n'
            data = data + text.encode('utf-8')
            print(text)
        
        log = open("log.txt", "w")
        log.write(data)
        log.close()

writeLog(site_ID, seller_IDs)