# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:18:53 2020

@author: 4PF41LA_RS6
"""

import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ['http://eluniversal.com.mx',]

    def parse(self, response):
        print("YOU'RE HERE:", response.url)
        next_pages = response.css("article a::attr(href)").getall()
        
        #print("HERE:", next_page)
        next_pages = set(next_pages)
        
        print(next_pages)
        
        with open("main_pages.txt", "w") as f:
            for item in next_pages:
                if "video" in item or "deporte" in item:
                    print("video or deporte")
                else:
                    f.write("%s\n" % item)
        
        """print("NEXT PAGES:")
        for p in next_pages:
            print(p)
        
        for page in next_pages:
            yield response.follow(page, callback = self.parse)"""