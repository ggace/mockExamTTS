from gtts import gTTS
import json

years = [2020]

isSpeakTopic = False;
isSpeakEng = True;
isSpeakKor = True;

for year in years:
    basicPath = rf"sources\{year}"
    resultPath = rf"output\{year}"

    problems = list(range(18, 25))+ list(range(29, 42)) + [43]
    
    
    for problem in problems:

        print(f"{year}년 11월 {problem}번 : start")

        with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        content = json_data["content"]
        topic = json_data["topic"]
        
        
        tts_number = gTTS(text=f"{year}년 {problem}번", lang='ko')

        
        if(topic != "" and isSpeakTopic):
            tts_topic = gTTS(text=f"주제 : {topic}", lang='ko')

        tts_contents = []
        for c in content:
            if(isSpeakEng):
                tts_contents.append(gTTS(text=c["eng"], lang='en'))
            if(isSpeakKor):
                tts_contents.append(gTTS(text=c["kor"], lang='ko'))
        
        
        fileName = rf"{resultPath}\{year}_{problem}"

        if(isSpeakTopic):
            fileName += "_topic"
        if(isSpeakKor):
            fileName += "_kor"
        if(isSpeakEng):
            fileName += "_eng"
        fileName += ".mp3"

        f = open(fileName,'wb') 
        tts_number.write_to_fp(f)
        if(topic != "" and isSpeakTopic):
            tts_topic.write_to_fp(f)
        for tts_content in tts_contents:
            tts_content.write_to_fp(f)
        f.close()

        print(f"{year}년 11월 {problem}번 : done")
    