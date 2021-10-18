from gtts import gTTS
import json

years = [2020]

for year in years:
    basicPath = rf"sources\{year}"
    resultPath = rf"output\{year}"

    problems = list(range(18, 25))+ list(range(29, 42)) + [43]

    for problem in problems:
        with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        content = json_data["content"]
        topic = json_data["topic"]
        
        tts_number = gTTS(text=f"{year}년 {problem}번", lang='ko')
        if(topic != ""):
            tts_topic = gTTS(text=f"주제 : {topic}", lang='ko')
        tts_content = gTTS(text=content, lang='en')
        
        
        fileName = rf"{resultPath}\{year}_{problem}.mp3"

        f = open(fileName,'wb') 
        tts_number.write_to_fp(f)
        if(topic != ""):
            tts_topic.write_to_fp(f)
        tts_content.write_to_fp(f)
        f.close()

        print(f"{year} : {problem}")
    