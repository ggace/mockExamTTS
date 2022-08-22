from gtts import gTTS
import json

years = [2021]

isSpeakTopic = True;
isSpeakEng = True;
isSpeakKor = True;

tags = []

if(isSpeakTopic):
    tags.append("topic")
if(isSpeakKor):
    tags.append("kor")
if(isSpeakEng):
    tags.append("eng")


for year in years:
    basicPath = rf"sources\{year}"
    resultPath = rf"output\{year}"

    problems = [20,21,22,23,24,29,30,31,32,33,34,35,36,37,38,39]
    
    
    for problem in problems:

        print(f"{year}년 9월 {problem}번 : start")

        with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        content = json_data["content"]
        topic = json_data["topic"]
        topicEng = json_data["topicEng"]
        
        
        tts_number = gTTS(text=f"{year}년 {problem}번", lang='ko')

        
        if(topic != "" and isSpeakTopic):
            tts_topic = gTTS(text=f"주제 : {topic}", lang='ko')
            tts_topicEng = gTTS(text=f"{topicEng}", lang='en')

        
        tts_contents = []
        
        if(isSpeakEng or isSpeakKor):
            tts_contents.append(gTTS(text=f"내용 : ", lang='ko'))
        for c in content:
            if(isSpeakEng):
                tts_contents.append(gTTS(text=c["eng"], lang='en'))
            if(isSpeakKor):
                tts_contents.append(gTTS(text=c["kor"], lang='ko'))
        
        
        fileName = rf"{resultPath}\{'_'.join(tags)}\{year}_{problem}"
        if(tags != ""):
            fileName += "_" + "_".join(tags)
        fileName += ".mp3"

        f = open(fileName,'wb') 
        tts_number.write_to_fp(f)
        if(topic != "" and isSpeakTopic):
            tts_topic.write_to_fp(f)
            tts_topicEng.write_to_fp(f)
        for tts_content in tts_contents:
            tts_content.write_to_fp(f)
        f.close()

        print(f"{year}년 9월 {problem}번 : done")
    