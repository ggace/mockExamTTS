from gtts import gTTS
import json

year = 2020
basicPath = rf"sources/{year}"
resultPath = rf"output/{year}"

problems = list(range(18, 25))+ list(range(29, 41))

for problem in problems:
    with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    content = json_data["content"]

    tts = gTTS(text=content, lang='en')
    tts.save(rf"{resultPath}\{year}_{problem}.mp3")
    