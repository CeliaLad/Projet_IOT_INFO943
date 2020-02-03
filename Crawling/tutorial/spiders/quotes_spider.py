# -*- coding: utf-8 -*-
import scrapy
import os
#response = requests.get("http://carlie-push-angel.e-monsite.com/")
            
     
# Récupère les éléments d'une page html et de la suivante, etc...
# scrapy crawl quotes -o quotes.json 
   
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        #'http://quotes.toscrape.com/page/1'
        'http://carlie-push-angel.e-monsite.com/'
    ]
    
    if (os.path.exists('E:\\PROJ943\\tutorial\\quotes.json') == True):
        os.remove('E:\\PROJ943\\tutorial\\quotes.json')
    
    def parse(self, response):
        for quote in response.css('div'):
            yield {
                'URL': quote.css('a::attr(href)').getall(),
            }
        

