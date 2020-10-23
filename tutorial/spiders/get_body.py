# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:45:19 2020

@author: 4PF41LA_RS6
"""

import scrapy

class NewsSpider(scrapy.Spider):
    name = "news2"
    start_urls = open("main_pages.txt", "r")
    page_number = 1

    def parse(self, response):
        print("\n ********* YOU'RE HERE ", self.page_number, response.url)
        self.page_number += 1
        #print("\n ***** Minuto x Minuto")
        mxm = response.css("div.view-content h2.field-content a::attr(href)").getall()
        
        """next_pages = response.css("article a::attr(href)").getall()
        
        print("HERE:", next_page)
        next_pages = set(next_pages)
        
        print(next_pages)
        
        with open("main_pages.txt", "w") as f:
            for item in next_pages:
                if "video" in item or "deporte" in item:
                    print("video or deporte")
                else:
                    f.write("%s\n" % item)
        
        print("NEXT PAGES:")
        for p in next_pages:
            print(p)
        
        for page in next_pages:
            yield response.follow(page, callback = self.parse)"""
        
        for page in mxm:
            if "video" in page or "deporte" in page:
                    print("video or deporte")
            elif "universal" in page:
                yield response.follow(page, callback = self.parse)