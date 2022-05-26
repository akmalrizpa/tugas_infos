import scrapy


class sintaubhara(scrapy.Spider):
    name = "ubhara"
    start_urls = ['https://www.ubhara.ac.id/v3/p/fasilitas']
    def parse(self, response):
        a = response.css('div.panel-body')
        judul = []
        isi = []
        for ab in a.css('p'):
            if ab.css('strong::text').get() != None:
                judul.append(ab.css('strong::text').get())
        for ba in a.css('ul'):
            tempo = []
            for bb in ba.css('li'):
                tempo.append(bb.css('li::text').get())
            isi.append(tempo)
        
        for a in range(3):
            yield{
                'judul' : judul[a],
                'isi' : isi[a]
            }

        