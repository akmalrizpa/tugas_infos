from webbrowser import get
import scrapy

class akmalrizpa(scrapy.Spider):

    name = 'akmalrizpa'

    start_urls = ['https://ukpim.my.id/event']

    def parse(self,response):
        juduls = response.css('.item-content')
        for judul in juduls:
            yield{
                "Nama Event" : judul.css('a::text').get(),
                "Waktu Event" : judul.css('.date::text').get(),
                "Status" : judul.css('.badge-pill::text').get()
            }