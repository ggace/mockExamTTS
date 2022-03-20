import pyttsx3
import json
from pydub import AudioSegment



engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 140)

korVoiceIndex = 0
EngVoiceIndex = 1

for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
    

years = [2021]

isSpeakTopic = False;
isSpeakEng = True;
isSpeakKor = False;

tags = []

if(isSpeakTopic):
    tags.append("topic")
if(isSpeakKor):
    tags.append("kor")
if(isSpeakEng):
    tags.append("eng")

problems = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

problemIndex = 0

for year in years:
    tempPath = rf"temps"
    basicPath = rf"..\sources\{year}"
    resultPath = rf"output/{year}"

    
    
    problems = [problems[problemIndex]]
    
    
    
    for problem in problems:
        
        
        fileName = rf"{resultPath}/{'_'.join(tags)}/{year}_{problem}"
        if(tags != ""):
            fileName += "_" + "_".join(tags)
        fileName += ".mp3"       
        
        engine.save_to_file("", fileName)
        engine.runAndWait()
        
        
        resultMp3 = AudioSegment.from_file(fileName)
         
        print(f"{year}년 11월 {problem}번 : start")

        with open(rf'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:
            json_data = json.load(f)
        content = json_data["content"]
        topic = json_data["topic"]
        topicEng = json_data["topicEng"]
        
        engine.setProperty('voice', voices[korVoiceIndex].id)
        engine.save_to_file(f"{year}년 {problem}번", tempPath + rf"/temp.mp3")
        engine.runAndWait()
        
        tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
        
        resultMp3 += tempMp3
        
        
        if(topic != "" and isSpeakTopic):
            engine.setProperty('voice', voices[korVoiceIndex].id)
            engine.save_to_file(f"주제 : {topic}", tempPath + rf"/temp.mp3")
            engine.runAndWait()
            tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
            resultMp3 += tempMp3
            engine.setProperty('voice', voices[EngVoiceIndex].id)
            engine.save_to_file(f"{topicEng}", tempPath + rf"/temp.mp3")
            engine.runAndWait()
            tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
            resultMp3 += tempMp3

        
        tts_contents = []
        
        if(isSpeakEng or isSpeakKor):
            engine.setProperty('voice', voices[korVoiceIndex].id)
            engine.save_to_file(f"내용 : ", tempPath + rf"/temp.mp3")
            engine.runAndWait()
            tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
            resultMp3 += tempMp3
        for c in content:
            if(isSpeakEng):
                engine.setProperty('voice', voices[EngVoiceIndex].id)
                engine.save_to_file(c["eng"], tempPath + rf"/temp.mp3")
                engine.runAndWait()
                tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
                resultMp3 += tempMp3
            if(isSpeakKor):
                engine.setProperty('voice', voices[korVoiceIndex].id)
                engine.save_to_file(c["kor"], tempPath + rf"/temp.mp3")
                engine.runAndWait()
                tempMp3 = AudioSegment.from_file(tempPath + rf"/temp.mp3")
                resultMp3 += tempMp3
        print(f"{year}년 11월 {problem}번 : done")
resultMp3.export(fileName, format="mp3")       
engine.stop()

        
        




