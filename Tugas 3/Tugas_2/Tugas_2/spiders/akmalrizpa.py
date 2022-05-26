import scrapy

class akmalrizpa(scrapy.Spider):
    name = 'akmalrizpa'
    start_urls = ['https://sinta.kemdikbud.go.id/affiliations/detail?id=2042&view=overview']

    def parse(self, response):
        baseUrl = 'https://sinta.kemdikbud.go.id'
        pathurl = response.css('a.hvr-grow')[2].attrib['href']
        urllengkap = f'{baseUrl}{pathurl}'
        yield response.follow(urllengkap,self.author)


    

    def author(self, response):
        rows = response.css('tr')
        for row in rows:
            if row.css('a.text-blue::text').get() != None:
                yield{
                    'Nama Dosen' : row.css('a.text-blue::text').get(),
                    'NIDN' : row.css('dd:nth-child(3)::text')[1].get().replace(' : ', ''),
                    '3 Years Score' : row.css('td:nth-child(2) > div:nth-child(1)::text').get(),
                    'All Years Score' : row.css('td:nth-child(3) > div:nth-child(1)::text').get()

                }
        
        try:
            baseUrl = 'https://sinta.kemdikbud.go.id/affiliations/detail'
            pathurl = response.css('ul.uk-pagination.uk-align-right.top-paging > li:nth-child(8) a').attrib['href']
            urllengkap = f'{baseUrl}{pathurl}'
            yield response.follow(urllengkap,self.author)
        except:
            pass