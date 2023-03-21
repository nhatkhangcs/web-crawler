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

8

NHATKHANG = [
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___01_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=149402&Expires=1679480021&Signature=QcHqYcU~7apAAQ1wduPbRQRMQC7p-Ndyd9NpsLG3IGZTv6loRsVjoPVp7K9dfF9U7UAh00w~earZWtNUojNqRFh7ERp6zherx6UHOfSl-gsgD5Z1whInuXf66hlbHrUxCbo6F1J1M-HepLDzxTWGFV-5ZRABPboloCaqa34hLGtPcYINhv15pvjykWJXgvnllzds2mlSzrLVnYYXtqK-LfSqfaqK477Ct6IXcXx-zzEFZXkaaFzWmOztJbPLV5Qayy1XO5RXU3-bvbyrMIyX30VDOAg9qUpE1AE3sbG6hiI91jhtCjgoxfpaYvjtGf4Tj3rph0PbiJcfp9eAo5RzhA__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___02_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=4870515&Expires=1679480048&Signature=cUbz6dS6gLfjwQFVTRZ4fi52hrN5KC86~55bNW-Z2KCyUwcSbXXW~NAyqBEZJxF3krY5yDIxRHJxRiuZTwIc8oKyMdLk-awj6R2tnIMCFJLfaJSO5zHCEkaJWKurqTTUiA9KFJtfGQpp0JV~F4C-SRrTdML-jlmuRByi3xffx843vJV3uf4~BmxVqujtk7AW3M0FdrmD0PPPONbrUBqzQ-KHHdRCz6XGu0lv4l1v~-gri55Kh8DO5CPdHAKJLORV9JQPNOGUOhceh4048caBIzNUsDjx62dagETDXG0IVuzhn292jyOaSboa4seogjX4b0MS40HxP-0tShDcWPBPQA__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___03_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=8930600&Expires=1679499130&Signature=Oy6C9~3uEOa~X2BW9Xp6JCZv8gvwrwzz62kNqqtEzwi24uSBpxg3TBPsqxYxjcfDe6nqSpHS49k7Wf8ggtAlRmPuWBKvyyX1bLPkDYqxo~Fy6YfhGmuIssx8NJpmCm8idrPi6dqodmOOCTeDrpFoJLXfrUxppjdTrW7OgEdZbu90QtkuCkRfd2~sjaTntBXoGtUzji5AKc9rne~qtJ60tX9Tr6rJ04dbRvO0PPIoMgyB1N7YE0cvIj0EDDjy6D6h-K1lvJnz75zwkcVg-KjiNXoMfyZOsMidD3UMg4XUBsahwGc9BxIVROTAD0FimiWdCejoRDcSnH5bA-g46oDRdw__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___04_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=1436663&Expires=1679499158&Signature=X5Pmrhu2CP9zvFPcEP~CdGPyUlfYkNTxxlvHEMl2IVn6aq-5VIfvEbqQFFFYUqnWxMnbfvxCG7FtF98vYLXsZurYoTp2IG6pIO~dLCvio40PgYCqaGwksLxQiqRSFEI~g6ZJkBz31YUxxtjmagw5QQUS~060zO4XaT~CHJZbpxe1Wk328PsQri26H6Es-XBUZRY2C~KfHWYj3vOTxgJUpeqVBJi4JMe55YJ0HWdGx107OtQmpO1eop2P5p~JskmEmKFRZCEoSRclF33SSjzEbF0NhFGhPxTERT92IgDePghpz8rokir56KICBzUrgQhMBdYKwiwN5WGeMbCb9AwNkw__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___05_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=1785000&Expires=1679499309&Signature=IOpUg91StWq9ErFSqmzYGkEEmROqtkkzeNX8U2O1ccJYYIFo0LEK5XF-s5UNgJSKFF5CTZXkCKVkBjnbg94c-2OZtTqcGOZI9SYQr2Q1v0bmjlxJGm8BuRdTPh9K7HTEF4fTHEUOlTxD~~nWlsLs1AVXGhfKhqBAAo1dyHkOvohrmYzNYJqx6qz3mFII2lIPPAjIpIkfuXrjOgMDDJdSzCuydTRzIjmtfLYL1vQhpseBvBno4qxicbyUkK0D9lQZHjrLWAtfwn1Pf7g4M37pSRwlH4AHrtDrqsjXhNccAd0qssVLXA6XAhyjpebZYV4nESjiNGo0-oZrYsj-6-eSIw__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___06_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=4951395&Expires=1679499350&Signature=fNz8kGMlHmP1OEin-CHSsTBtfEoJPlkps7u-5x7B8xfbrpzvojVFyDMLmX22ERwU2ZRQu7MOxBRMbbXZ7Rinsx4xNscTMrfbU1eO5E0VM5PlJXEY7nK6x~6opmJRawNLl~gf0XrrscENGu7YzFc0I35vXk6x6NwoilvGSSrjjLMXW-EovPTNavqRVbH4caNlAgWgbEzEriDKxXjG02XlO1Bvd-CSqKeL31Rr63naxewC1Uu1njS6NMa~mYD5AQ4DW6LtNdJvT~bGhGklDlnLiJJ-Z8XuehKPrg25BhpaP6-om-ibCjijP32JUGO5jTFGeQi2GaHN-dq9r0CsTOmUpQ__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___07_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=3174508&Expires=1679499376&Signature=flP2waHXjqycmJ1NdKQnCS4PIOcw8zaoOkbWNvIF9mtpLlB9appGZxaSrG3Zl5wKE3RgjNfzjOaebpPBdYsZredVJBVL6JLJ6IfZTOfvjtF6TO05ycs4ZjQHm5SFk-IISH5Fi7aBIgodWB5G0I8Av5qfZWOysPjVoJA1Di05r8bZXFdgo1Fc3WcSezTbbo5CsR9z7rCBg~iV9rjJ5wbZ-0oEdqqEDVeA~2A5TqaDb6CuvjCjxMyfIu~6O5ZTHtEncPYZUwk-xWpO4c38mjTWeJvRz0yTUFgjMNqBX24CYKIm3ybbfuku1XrfL-8-G2dFimScRRxl2uyPnlHeLCe50A__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___08_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=8704569&Expires=1679499419&Signature=Kt4sTRx2zJmgQKSXz693aNQHySnRBSzhvbDEy8QybJ8TR2B9AFzp0CuarYCvMoOcG5fVwUqM6gblXW7uyxTyUwNDdn7Oh9j1aU2Zanzl5l61DgvD3T~Vm~bfxIgAIgr~nhFjSUv9Rl~rV8tYQx~W1W1RmcsSZTLJPIWSgP7s2V9YmcGxz~vh7zhNtI8t5vk3~8-vxe6WA~ERdjfXljDnqbeCd3d5bGRfEaJHuZl8~GqliddaXXNWnRlkyrYwjoNERrHpv9zRFneErTJGdSdlZZs6fODepZhRj7VSHTxBnjshq4n1HK3T~vx6JrjqGoPdWk04IL8XvCIeVYDpA-CvRQ__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___09_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=9964997&Expires=1679499438&Signature=QTqjMH~HeNqzw181kkTbLAosxkP1rqVPALT~rNjhJKLJsuXRAw~cfZbzkP7kfOBUlRXv0xYpKn1joZV2t3ZVIU4LrZc1Sp~FFyj14DQoaAo4iQGryywfRVYCr0zu22X~~W5zmE0GgsKN-XFT5pdel0uUOybt3t~vByRzR7I9bfRUhg2Z706UXAow3YORCyq3vQm3PKm-wWublP6PNianf7tB~Cu5WQXUxGVvSh~TQtjXRgKZtiB0ncdWAtKR7xmtfIi0watRsDUQ5H68EAiKbQWlxI~IMyqXR73UESJ6kHvV2ni5xvbZ9EN~iQdeQis9GXxwQfNUsnVLODd4Yaluww__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___10_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=4405463&Expires=1679499452&Signature=M82RKnf0o9SQEmrBmS7a2DTecrNWtQK9SPxzdypRPRzaXcoajOxk9ydJhv0YNGA88mUhwt5cmp5idtL6~4WgcywGIkEveUolrfjvymRNP7l65Ba8UCD7~oxzvNyoNiqmv0lGXnLRh~-JHk883RU0p5hxsu~-BnE~P55mTKRWaUDGHuT-0i4V-6hGPZc7qSlFnF~w4rkwwSoP7I-DyPovwJ6brh8Q7nCzV4XyOLdML1KzDsNm8N0Z3FJuAQW4OKTGh6MLG9ZbhM~ob3YeHBZYf3Jst~6RcggL~jSBP3zxDzeywprrXKA-f4SNymVwwsxAhc9XLR2sQjvLhIu3tK6X2Q__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___11_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=1225716&Expires=1679499463&Signature=PM9E~n4Y57bb2SJe4FA0nFZ5iGE3gB~eyRqj1apppdZNYo6xA1f73sBUShFBt7opQcpPkK~UKqhwFclwYKXXVSoV0VyaAqtaobtkd4XWM-bwMHhhhWEotiypFRK2CLykEOsDmeuHj2jM03AKoJCsTo7wOkDMa-h7WBXFodXUe1mzHMMmYHpr2rB~WGj6TZ4AztbnGmJQEfewgWvtxFec9OcavBsJQkCqVJr994iUlQw-W-Jpyy6G7aJK05pJs4Byk0djgK-WDpSeqvX8-03eMXtpiRB2GIxqA~MBxxlghkLpXFmdVN~b59CFy5AXCSXky1bNKMvZtyn9WvH4ZJT3ow__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___12_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=5565173&Expires=1679499473&Signature=cjub0orZX-5fit7r0NGnrInrjFwS134k9VA~-r3X6ZB-wqH4djbHOs-uTjvbjKPlFBaaXvk1~O6selI9peAgqcIM8Lv4IHwj1s2LmkRXbT~QX8SrApu7JQanNlyKgDiTlpbm0hdta1i6nravTyWEw53vGqChRg625nYp5Jc3CL9FvY-5UcIx4-ZI-kqElez0iVV8m40l5a6SYJHl~ora71ErWa0kFLrHJxi8nnmLh578N0O-cQ77MkpY8fmSxF4e9~BZavIVFKvsMMpKEQce0bcHodEAqUa21bQzlTjmJyb7CDp0TR7NE3973at3miv3hUpi2GcFfww0egpFVuCTvQ__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___13_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=8431555&Expires=1679499487&Signature=b1ANW4Qd2JHebGMoQVE78M7cy6h7wU8SypoVwDdH3S~9bqd8frWLXBjkOFbfoGLQ75IdayNjvT-qVNsqImtKwSY0G3frUe-MPCUUnLkZo6wGFqHoCQXvoFm1jYVbQCcDcPmvVSIs-0xrMIR9oVhQCskTQ2ob2ajBaFsdo-68xWc4e6c0cO-~6hmqBthX6EGYHHYmg0A9T5U7npXz2l1ecid51Cj0EP9vMTmi-Dqhwe2PZPz2Q4ofAqwbfWvslzQM1Q0STIIaqNGESzP~fhUTOEw~IkHITxrbnuZf4ccmqjpG10IU6Q63PqEdr9kPuCnF2iG52xe4D6jRdU5UIneihg__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___14_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=4442143&Expires=1679499500&Signature=IXp2PG5-2jjiKJCZAfYxR3DyL9qu-b2thrEal0pJIhe0OY13T0btF97weatKwE9PEKpcWsPVSHos-uBYKJ8vGW1r~yVCQ~tgpR1c1FgnYu2feZwv-GUjYqXW4tJkpO1zh8jGKDZhqC--2q9jwdYaEDDfqhHpLgocHGfk8xit5ibDN-rIbOB04BVlRDS8ojNiJ78I751sosuwCgMJAI9h3WSJd4aBa4VPM1xwRYR2SIxf5d3~5ctX2-ygWpS1WtSV2xSosts0ZhuqP3qwoJrBGL80cIpY3oTtU16R27Z8dSH5INaKsoe9RC3GTfxXjhoyjV~R9b7WypkuO1MTYr9Wsw__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___15_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=1546946&Expires=1679499511&Signature=SA42Ks1H~ozVbS6o53RfPkLLR98K3cPKQAlltrJWRfF-6NAcKX1BLuygfzUUGfDPPvmAyqTGkiM8pmIOAIthxWCfhQAhyaPSgCvteJAkqYjnIdGzm1-8Zc6zMWoYAAWShyZa8-EOEIF9fiBjCRD-uS9udnE9zp2LUG8W~yBdIPR82QXYEuHsoKysp~fxkOI61VsdVVMoBoOQ9-BWQ7TDQdgQoZ4Ml8GlFHRBZxTKlU-N36jewD1ymPJfMRil5Xnja2r-AJ8jSuKIwEh3InNRUoj8bwd0r48GunhrnzYLkS3A-QElVxQIPXaS5VVhAcBdgzm~zViqimS71SvQ4eQzkA__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___16_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=7937632&Expires=1679499523&Signature=P9E0U5gZ1BBGCarAHLdwje6Tt1hjFdTInaYWtGwtVhlb4--TUe5rI9uuTdgwQ-7wGapuTrLiiis3hT74ZFjKwflF2EzwlWat3nHq0i~XBVQkIE6doofcpy7xZK5D7l~49~c5Cc5gKnwuRAqwVLV~cloJyZq2vBZA3kAJVvfxai6JdcbH9ZA7vP~dmo2-PrHLjZQV6waWCTsJK9aS51tjKdZZrGJO-PC4By~kYW8BNF21OgcZo7dgTny6VuRIsQ96PtNfTt9R3m0TW7w0sHJOw4nsB6-lYbvw4obQd1DG~YUEAabiWYc4tjvBOdY7D8plbBEfvF7ksClxokMXaC7mng__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___17_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=3253337&Expires=1679499561&Signature=TnqHl-NjWleMXy6ks6DPjtPqr2TuXroqpI~lt1rfT~KlmwZEje2X0hYr1g7kAxI6B0EzUdXRuxKerYS6Q4KhJxjMzqxovCtQ0N37edNMFNRL1o7sR-6xEeYOQJB5BlyuaLXEgT-WL~ytp9cHaWYIr94aSQax2LU3OrebjgVEDCaV26GoMsIH35hTrgyiNezO74NQPi4sS5gbWtwO39fU-kAEdKe-lU7lwIj4Jgdfa9z5FE9-XLu7U8~PdZz0Rw2mmd2Ivuky7v-ByNd9NFPz-CBTu-DvpxM5BWsiGSYk-Y6arxCfO~jM8rv4SX5U9espYWGQYV8w9Et6YMPwVwh5Ww__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "https://content.cdn.dbp-prod.dbp4.org/audio/BDQDVS/BDQDVSN2DA/B01___18_Matthew_____BDQDVSN2DA.mp3?x-amz-transaction=2173337&Expires=1679499609&Signature=Y7C~gmKKiU5tixTgGqqMUHuk5L4utLW2ztRKVQgmHeBtY7BCU6TAen3uNWBzoSVxNZ5vAm0JwgzJZ7JV95obDmltLfUR2rBdaCMvKo5AArBrzfflvCRg9bo4lbxQh1uzaeZMlXPxCZ3cjGJ~4wtHiQw6kg3msxk44PE0eIlrBWpNvs9JlpwuT8BSu7PzKWd9I6g11jeg5xIguwh8pM4GSNtcxlz-NSX1JGIp3Fw8wprxIn4ObXTVAPRmYLkMAi6B40~a94Zl~f8XTaD4kms~FqISADzzc7uBQfiqauvsC8whYwyXBSmaAuX2rCYq6XQX1BKLtozrFhunF~EqWfxChA__&Key-Pair-Id=APKAI4ULLVMANLYYPTLQ",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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


i = 1
for url in NHATKHANG:
    response = requests.get(url)
    
    # Save the downloaded content to a file on disk
    with open("audios/audio{i}.mp3", 'wb') as f:
        f.write(response.content)

    i = i + 1
    # Convert the downloaded file to a desired format (e.g. WAV)
