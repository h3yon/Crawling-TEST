from wordcloud import WordCloud

text = ''
with open("kakao.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line

print(text)

wc = WordCloud(font_path='/System/Library/Fonts/AppleSDGothicNeo.ttc', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
