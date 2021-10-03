from wordcloud import WordCloud
from PIL import Image
import numpy as np
import random

text = ''
with open("kakao.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        result = line.split(',"')
        if len(result) == 3:
            text += result[2].replace('ㅋ','').replace('ㅠ','').replace('채널추가하고','').replace('ㅜ','').replace('이모티콘','').replace('사진','').replace('"','')

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# mask = np.array(Image.open('cloud.png'))
mask = np.array(Image.open('sherlock.png'))
wc = WordCloud(font_path='/Users/we/Library/Fonts/SCDream5.otf', background_color="Black", mask=mask, max_font_size=100)
wc.generate(text)
wc.recolor(color_func=grey_color_func)
wc.to_file("sherlock_masked.png")
