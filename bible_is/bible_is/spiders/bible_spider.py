import scrapy

class BibleSpider(scrapy.Spider):
    name = 'bible'
    allowed_domains = ['live.bible.is']
    start_urls = ['http://live.bible.is/bible/BDQDVS/MAT/1']

    def parse(self, response):
        verses = response.css('.verse')
        for verse in verses:
            verse_number = verse.css('.verseNumber::text').get()
            verse_text = verse.css('.verseText::text').get()
            print(f"{verse_number}: {verse_text}")
