import scrapy
import time
import random
import os
import requests
import subprocess

WORK_DIR = '/Users/khangnguyen/lab/bahnar_tts/bible'
LANG = ['BDQDVS', 'VIEBIB']

BASE_URL = 'https://live.bible.is/bible'
PATHS = [
    "MAT/1?audio_type=audio_drama",
    "MAT/2?audio_type=audio_drama",
    "MAT/3?audio_type=audio_drama",
    "MAT/4?audio_type=audio_drama",
    "MAT/5?audio_type=audio_drama",
    "MAT/6?audio_type=audio_drama",
    "MAT/7?audio_type=audio_drama",
    "MAT/8?audio_type=audio_drama",
    "MAT/9?audio_type=audio_drama",
    "MAT/10?audio_type=audio_drama",
    "MAT/11?audio_type=audio_drama",
    "MAT/12?audio_type=audio_drama",
    "MAT/13?audio_type=audio_drama",
    "MAT/14?audio_type=audio_drama",
    "MAT/15?audio_type=audio_drama",
    "MAT/16?audio_type=audio_drama",
    "MAT/17?audio_type=audio_drama",
    "MAT/18?audio_type=audio_drama",
    "MAT/19?audio_type=audio_drama",
    "MAT/20?audio_type=audio_drama",
    "MAT/21?audio_type=audio_drama",
    "MAT/22?audio_type=audio_drama",
    "MAT/23?audio_type=audio_drama",
    "MAT/24?audio_type=audio_drama",
    "MAT/25?audio_type=audio_drama",
    "MAT/26?audio_type=audio_drama",
    "MAT/27?audio_type=audio_drama",
    "MAT/28?audio_type=audio_drama",
    "MRK/1?audio_type=audio_drama",
    "MRK/2?audio_type=audio_drama",
    "MRK/3?audio_type=audio_drama",
    "MRK/4?audio_type=audio_drama",
    "MRK/5?audio_type=audio_drama",
    "MRK/6?audio_type=audio_drama",
    "MRK/7?audio_type=audio_drama",
    "MRK/8?audio_type=audio_drama",
    "MRK/9?audio_type=audio_drama",
    "MRK/10?audio_type=audio_drama",
    "MRK/11?audio_type=audio_drama",
    "MRK/12?audio_type=audio_drama",
    "MRK/13?audio_type=audio_drama",
    "MRK/14?audio_type=audio_drama",
    "MRK/15?audio_type=audio_drama",
    "MRK/16?audio_type=audio_drama",
    "LUK/1?audio_type=audio_drama",
    "LUK/2?audio_type=audio_drama",
    "LUK/3?audio_type=audio_drama",
    "LUK/4?audio_type=audio_drama",
    "LUK/5?audio_type=audio_drama",
    "LUK/6?audio_type=audio_drama",
    "LUK/7?audio_type=audio_drama",
    "LUK/8?audio_type=audio_drama",
    "LUK/9?audio_type=audio_drama",
    "LUK/10?audio_type=audio_drama",
    "LUK/11?audio_type=audio_drama",
    "LUK/12?audio_type=audio_drama",
    "LUK/13?audio_type=audio_drama",
    "LUK/14?audio_type=audio_drama",
    "LUK/15?audio_type=audio_drama",
    "LUK/16?audio_type=audio_drama",
    "LUK/17?audio_type=audio_drama",
    "LUK/18?audio_type=audio_drama",
    "LUK/19?audio_type=audio_drama",
    "LUK/20?audio_type=audio_drama",
    "LUK/21?audio_type=audio_drama",
    "LUK/22?audio_type=audio_drama",
    "LUK/23?audio_type=audio_drama",
    "LUK/24?audio_type=audio_drama",
    "JHN/1?audio_type=audio_drama",
    "JHN/2?audio_type=audio_drama",
    "JHN/3?audio_type=audio_drama",
    "JHN/4?audio_type=audio_drama",
    "JHN/5?audio_type=audio_drama",
    "JHN/6?audio_type=audio_drama",
    "JHN/7?audio_type=audio_drama",
    "JHN/8?audio_type=audio_drama",
    "JHN/9?audio_type=audio_drama",
    "JHN/10?audio_type=audio_drama",
    "JHN/11?audio_type=audio_drama",
    "JHN/12?audio_type=audio_drama",
    "JHN/13?audio_type=audio_drama",
    "JHN/14?audio_type=audio_drama",
    "JHN/15?audio_type=audio_drama",
    "JHN/16?audio_type=audio_drama",
    "JHN/17?audio_type=audio_drama",
    "JHN/18?audio_type=audio_drama",
    "JHN/19?audio_type=audio_drama",
    "JHN/20?audio_type=audio_drama",
    "JHN/21?audio_type=audio_drama",
    "ACT/1?audio_type=audio_drama",
    "ACT/2?audio_type=audio_drama",
    "ACT/3?audio_type=audio_drama",
    "ACT/4?audio_type=audio_drama",
    "ACT/5?audio_type=audio_drama",
    "ACT/6?audio_type=audio_drama",
    "ACT/7?audio_type=audio_drama",
    "ACT/8?audio_type=audio_drama",
    "ACT/9?audio_type=audio_drama",
    "ACT/10?audio_type=audio_drama",
    "ACT/11?audio_type=audio_drama",
    "ACT/12?audio_type=audio_drama",
    "ACT/13?audio_type=audio_drama",
    "ACT/14?audio_type=audio_drama",
    "ACT/15?audio_type=audio_drama",
    "ACT/16?audio_type=audio_drama",
    "ACT/17?audio_type=audio_drama",
    "ACT/18?audio_type=audio_drama",
    "ACT/19?audio_type=audio_drama",
    "ACT/20?audio_type=audio_drama",
    "ACT/21?audio_type=audio_drama",
    "ACT/22?audio_type=audio_drama",
    "ACT/23?audio_type=audio_drama",
    "ACT/24?audio_type=audio_drama",
    "ACT/25?audio_type=audio_drama",
    "ACT/26?audio_type=audio_drama",
    "ACT/27?audio_type=audio_drama",
    "ACT/28?audio_type=audio_drama",
    "ROM/1?audio_type=audio_drama",







    
    "ROM/2?audio_type=audio_drama",
    "ROM/3?audio_type=audio_drama",
    "ROM/4?audio_type=audio_drama",
    "ROM/5?audio_type=audio_drama",
    "ROM/6?audio_type=audio_drama",
    "ROM/7?audio_type=audio_drama",
    "ROM/8?audio_type=audio_drama",
    "ROM/9?audio_type=audio_drama",
    "ROM/10?audio_type=audio_drama",
    "ROM/11?audio_type=audio_drama",
    "ROM/12?audio_type=audio_drama",
    "ROM/13?audio_type=audio_drama",
    "ROM/14?audio_type=audio_drama",
    "ROM/15?audio_type=audio_drama",
    "ROM/16?audio_type=audio_drama",
    "1CO/1?audio_type=audio_drama",
    "1CO/2?audio_type=audio_drama",
    "1CO/3?audio_type=audio_drama",
    "1CO/4?audio_type=audio_drama",
    "1CO/5?audio_type=audio_drama",
    "1CO/6?audio_type=audio_drama",
    "1CO/7?audio_type=audio_drama",
    "1CO/8?audio_type=audio_drama",
    "1CO/9?audio_type=audio_drama",
    "1CO/10?audio_type=audio_drama",
    "1CO/11?audio_type=audio_drama",
    "1CO/12?audio_type=audio_drama",
    "1CO/13?audio_type=audio_drama",
    "1CO/14?audio_type=audio_drama",
    "1CO/15?audio_type=audio_drama",
    "1CO/16?audio_type=audio_drama",
    "2CO/1?audio_type=audio_drama",
    "2CO/2?audio_type=audio_drama",
    "2CO/3?audio_type=audio_drama",
    "2CO/4?audio_type=audio_drama",
    "2CO/5?audio_type=audio_drama",
    "2CO/6?audio_type=audio_drama",
    "2CO/7?audio_type=audio_drama",
    "2CO/8?audio_type=audio_drama",
    "2CO/9?audio_type=audio_drama",
    "2CO/10?audio_type=audio_drama",
    "2CO/11?audio_type=audio_drama",
    "2CO/12?audio_type=audio_drama",
    "2CO/13?audio_type=audio_drama",
    "GAL/1?audio_type=audio_drama",
    "GAL/2?audio_type=audio_drama",
    "GAL/3?audio_type=audio_drama",
    "GAL/4?audio_type=audio_drama",
    "GAL/5?audio_type=audio_drama",
    "GAL/6?audio_type=audio_drama",
    "EPH/1?audio_type=audio_drama",
    "EPH/2?audio_type=audio_drama",
    "EPH/3?audio_type=audio_drama",
    "EPH/4?audio_type=audio_drama",
    "EPH/5?audio_type=audio_drama",
    "EPH/6?audio_type=audio_drama",
    "PHP/1?audio_type=audio_drama",
    "PHP/2?audio_type=audio_drama",
    "PHP/3?audio_type=audio_drama",
    "PHP/4?audio_type=audio_drama",
    "COL/1?audio_type=audio_drama",
    "COL/2?audio_type=audio_drama",
    "COL/3?audio_type=audio_drama",
    "COL/4?audio_type=audio_drama",
    "1TH/1?audio_type=audio_drama",
    "1TH/2?audio_type=audio_drama",
    "1TH/3?audio_type=audio_drama",
    "1TH/4?audio_type=audio_drama",
    "1TH/5?audio_type=audio_drama",
    "2TH/1?audio_type=audio_drama",
    "2TH/2?audio_type=audio_drama",
    "2TH/3?audio_type=audio_drama",
    "1TI/1?audio_type=audio_drama",
    "1TI/2?audio_type=audio_drama",
    "1TI/3?audio_type=audio_drama",
    "1TI/4?audio_type=audio_drama",
    "1TI/5?audio_type=audio_drama",
    "1TI/6?audio_type=audio_drama",
    "2TI/1?audio_type=audio_drama",
    "2TI/2?audio_type=audio_drama",
    "2TI/3?audio_type=audio_drama",
    "2TI/4?audio_type=audio_drama",
    "TIT/1?audio_type=audio_drama",
    "TIT/2?audio_type=audio_drama",
    "TIT/3?audio_type=audio_drama",
    "PHM/1?audio_type=audio_drama",
    "HEB/1?audio_type=audio_drama",
    "HEB/2?audio_type=audio_drama",
    "HEB/3?audio_type=audio_drama",
    "HEB/4?audio_type=audio_drama",
    "HEB/5?audio_type=audio_drama",
    "HEB/6?audio_type=audio_drama",
    "HEB/7?audio_type=audio_drama",
    "HEB/8?audio_type=audio_drama",
    "HEB/9?audio_type=audio_drama",
    "HEB/10?audio_type=audio_drama",
    "HEB/11?audio_type=audio_drama",
    "HEB/12?audio_type=audio_drama",
    "HEB/13?audio_type=audio_drama",
    "JAS/1?audio_type=audio_drama",
    "JAS/2?audio_type=audio_drama",
    "JAS/3?audio_type=audio_drama",
    "JAS/4?audio_type=audio_drama",
    "JAS/5?audio_type=audio_drama",
    "1PE/1?audio_type=audio_drama",
    "1PE/2?audio_type=audio_drama",
    "1PE/3?audio_type=audio_drama",
    "1PE/4?audio_type=audio_drama",
    "1PE/5?audio_type=audio_drama",
    "2PE/1?audio_type=audio_drama",
    "2PE/2?audio_type=audio_drama",
    "2PE/3?audio_type=audio_drama",
    "1JN/1?audio_type=audio_drama",
    "1JN/2?audio_type=audio_drama",
    "1JN/3?audio_type=audio_drama",
    "1JN/4?audio_type=audio_drama",
    "1JN/5?audio_type=audio_drama",
    "2JN/1?audio_type=audio_drama",
    "3JN/1?audio_type=audio_drama",
    "JUD/1?audio_type=audio_drama",
    "REV/1?audio_type=audio_drama",
    "REV/2?audio_type=audio_drama",
    "REV/3?audio_type=audio_drama",
    "REV/4?audio_type=audio_drama",
    "REV/5?audio_type=audio_drama",
    "REV/6?audio_type=audio_drama",
    "REV/7?audio_type=audio_drama",
    "REV/8?audio_type=audio_drama",
    "REV/9?audio_type=audio_drama",
    "REV/10?audio_type=audio_drama",
    "REV/11?audio_type=audio_drama",
    "REV/12?audio_type=audio_drama",
    "REV/13?audio_type=audio_drama",
    "REV/14?audio_type=audio_drama",
    "REV/15?audio_type=audio_drama",
    "REV/16?audio_type=audio_drama",
    "REV/17?audio_type=audio_drama",
    "REV/18?audio_type=audio_drama",
    "REV/19?audio_type=audio_drama",
    "REV/20?audio_type=audio_drama",
    "REV/21?audio_type=audio_drama",
    "REV/22?audio_type=audio_drama"
]

def assemble_bible_url(language, path):
    if language == "bahnar":
        return BASE_URL + LANG[0] + path
    elif language == "vie":
        return BASE_URL + LANG[1] + path


def write_text_2_dir_file(current_url, content, is_Vie_lang=0):
    #    https://live.bible.is/bible/BDQDVS/MAT/1?audio_type=audio_drama
    # => BDQDVS_MAT_1
    name_segments = current_url.replace('?', '/').split('/')[4:7]
    text_file_name = '_'.join(name_segments)
    if not os.path.exists(f'{WORK_DIR}/{LANG[is_Vie_lang]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[is_Vie_lang]}')
    if not os.path.exists(f'{WORK_DIR}/{LANG[is_Vie_lang]}/{name_segments[1]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[is_Vie_lang]}/{name_segments[1]}')
    with open(f'{WORK_DIR}/{LANG[is_Vie_lang]}/{name_segments[1]}/{text_file_name}.txt', 'w') as f:
        f.write(content)


def write_audio_link_2_file(current_url, content, is_Vie_lang=0):
    #    https://live.bible.is/bible/BDQDVS/MAT/1?audio_type=audio_drama
    # => BDQDVS_MAT_1
    with open(f'{WORK_DIR}/BahnarAudioLinks.txt', 'a') as f:
        f.write(content)


class BibleSpider(scrapy.Spider):
    name = 'bible'
    start_urls = [assemble_bible_url(language="bahnar", path=PATHS[0])]
    current_url = start_urls[0]
    index = 0

    def parse(self, response):

        # Scraping text:
        """
        """
        chapter_text = response.css('div.justify').css('::text').getall()
        filtered_chapter_text = [verse for verse in chapter_text
                                 if not (verse.isdigit() or
                                         (verse[0] == '"' and verse[1:-1].isdigit()) or verse == "\xa0")]
        complete_chapter = ''.join(filtered_chapter_text).strip()
        # write to a file with appropriate name
        write_text_2_dir_file(self.current_url, complete_chapter, 1)
        # Scraping audio

        try:
            next_page = assemble_bible_url(
                language="bahnar", path=PATHS[self.index])
            self.current_url = next_page
            self.index += 1
            time.sleep(random.randint(10, 40))
            yield response.follow(next_page, callback=self.parse)
        except IndexError:
            return