from gtts import gTTS
import json

year = 2019
basicPath = rf"sources/{year}"
resultPath = rf"output/{year}"

problems = list(range(18, 25))+ list(range(29, 41))

for problem in problems:
    with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    content = json_data["content"]
    
    tts_number = gTTS(text=f"{year}년 {problem}번", lang='ko')
    tts_content = gTTS(text=content, lang='en')
    
    fileName = rf"{resultPath}\{year}_{problem}.mp3"

    f = open(fileName,'wb') 
    tts_number.write_to_fp(f)
    tts_content.write_to_fp(f)
    f.close()
    