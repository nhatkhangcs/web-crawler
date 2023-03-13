import scrapy
import time
import random
import os

BASE_URL = 'https://live.bible.is'
NEXT_URLS = [
    f"{BASE_URL}/bible/BDQDVS/MAT/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/17?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/18?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/19?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/20?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/21?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/22?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/23?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/24?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/25?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/26?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/27?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MAT/28?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/MRK/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/17?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/18?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/19?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/20?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/21?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/22?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/23?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/LUK/24?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/17?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/18?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/19?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/20?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JHN/21?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/17?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/18?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/19?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/20?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/21?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/22?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/23?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/24?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/25?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/26?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/27?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ACT/28?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/ROM/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1CO/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2CO/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/GAL/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/EPH/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/PHP/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/PHP/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/PHP/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/PHP/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/COL/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/COL/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/COL/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/COL/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TH/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TH/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TH/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TH/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TH/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TH/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TH/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TH/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1TI/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TI/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TI/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TI/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2TI/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/TIT/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/TIT/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/TIT/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/PHM/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/HEB/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JAS/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JAS/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JAS/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JAS/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JAS/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1PE/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1PE/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1PE/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1PE/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1PE/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2PE/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2PE/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2PE/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1JN/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1JN/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1JN/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1JN/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/1JN/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/2JN/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/3JN/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/JUD/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/1?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/2?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/3?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/4?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/5?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/6?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/7?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/8?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/9?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/10?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/11?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/12?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/13?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/14?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/15?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/16?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/17?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/18?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/19?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/20?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/21?audio_type=audio_drama",
    f"{BASE_URL}/bible/BDQDVS/REV/22?audio_type=audio_drama"
]
WORK_DIR = '/Users/khangnguyen/lab/bahnar_tts/bible'
LANG = ['BDQDVS', 'VIEBIB']
def write_text_2_dir_file(current_url, content, vie_lang=0):
    #    https://live.bible.is/bible/BDQDVS/MAT/1?audio_type=audio_drama
    # => BDQDVS_MAT_1
    name_segments = current_url.replace('?', '/').split('/')[4:7]
    text_file_name = '_'.join(name_segments)
    if not os.path.exists(f'{WORK_DIR}/{LANG[vie_lang]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[vie_lang]}')
    if not os.path.exists(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}')
    with open(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}/{text_file_name}.txt', 'w') as f:
        f.write(content)
def save_audio(current_url, content, vie_lang=0)
    #    https://live.bible.is/bible/BDQDVS/MAT/1?audio_type=audio_drama
    # => BDQDVS_MAT_1
    name_segments = current_url.replace('?', '/').split('/')[4:7]
    text_file_name = '_'.join(name_segments)
    if not os.path.exists(f'{WORK_DIR}/{LANG[vie_lang]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[vie_lang]}')
    if not os.path.exists(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}'):
        os.mkdir(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}')
    with open(f'{WORK_DIR}/{LANG[vie_lang]}/{name_segments[1]}/{text_file_name}.txt', 'w') as f:
        f.write(content)

class BibleSpider(scrapy.Spider):
    name = 'bible'
    start_urls = ['https://live.bible.is/bible/BDQDVS/MAT/1?audio_type=audio_drama']
    current_url = start_urls[0]
    index = 0
    def parse(self, response):

        # Scraping text:
        """
        chapter_text = response.css('div.justify').css('::text').getall()
        filtered_chapter_text = [verse for verse in chapter_text
                                 if not (verse.isdigit() or
                                         (verse[0] == '"' and verse[1:-1].isdigit()) or verse == "\xa0")]
        complete_chapter = ''.join(filtered_chapter_text).strip()
        # write to a file with appropriate name
        write_text_2_dir_file(self.current_url, complete_chapter)
        """
        # Scraping audio

        try:
            next_page = NEXT_URLS[self.index]
            self.current_url = next_page
            self.index += 1
            time.sleep(random.randint(10, 40))
            yield response.follow(next_page, callback = self.parse)
        except IndexError:
            return
    """
    SCRAPING TEXT:
    get text from div.justify (into an array)
    rid the array of \xa0 and numbers
    join elements into a passage
    write the passage to a plain text file with proper name 
    """
    """
    SCRAPING AUDIO:
    
    """
