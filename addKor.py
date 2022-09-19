string = """From the earliest times, healthcare services have been recognized to have two equal aspects, namely clinical care and public healthcare.

가장 초기의 시대부터, 헬스케어 서비스는 두 가지의 동등한 영역, 즉 병원 치료와 공공 헬스케어를 포함하는 것으로 인식되어 왔다.

In classical Greek mythology, the god of medicine, Asklepios, had two daughters, Hygiea and Panacea.

고대 그리스 신화에서 의료의 신 아스클레피오스에게는 하이지아와 파나시아라는 두 딸이 있었다. 

The former was the goddess of preventive health and wellness, or hygiene, and the latter the goddess of treatment
and curing.

전자는 예방적 건강과 건강 관리, 즉 위생의 여신이었고, 후자는 치료와 치유의 여신이었다.

In modern times, the societal ascendancy of medical professionalism has caused treatment of sick patients to
overshadow those preventive healthcare services provided by the less heroic figures of sanitary engineers,
biologists, and governmental public health officers.

현대 시대에, 의료 전문성에 대한 사회적 우세는 아픈 환자들의 치료가 위생 공학자, 생물학자, 정부 공공 건강 관료와 같은 덜 영웅적인 인물들에 의해서 제공되는
그러한 예방적 헬스케어 서비스를 가리도록 만들었다. 

Nevertheless, the quality of health that human populations enjoy is attributable less to surgical dexterity, innovative
pharmaceutical products, and bioengineered devices than to the availability of public sanitation, sewage
management, and services which control the pollution of the air, drinking water, urban noise, and food for human
consumption.

그럼에도 불구하고, 인류가 향유하는 건강의 질은 공공 위생, 하수 관리 그리고 대기 오염, 식수, 도시 소음, 인간이 소비하는 음식을 관리하는 서비스들의 이용 가능성에 비해
수술적 기민함, 혁신적 제약 제품, 그리고 생물 공학적 장비에 덜 기인한다. 

The human right to the highest attainable standard of health depends on public healthcare services no less than on the skills and equipment of doctors and hospitals.

건강에 대한 달성 가능한 최고 수준에 대한 인간의 권리는 의사와 병원의 기술과 장비만큼이나 공공 헬스케어 서비스에 달려 있다"""

string = ".\n".join(" ".join((" ".join(string.split("\n\n")[1::2])).split("\n")).split(". "))



import json

basicPath = r"sources\2022"
problem = 24

string = string.strip()
stringPart = string.split("\n")

with open(f'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:

    json_data = json.load(f)
print("\n".join(stringPart))

for i in range(len(stringPart)):
    json_data["content"][i]["kor"] = stringPart[i]
    


with open(f'{basicPath}\{problem}.json', 'w', encoding='UTF8') as make_file:

    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)



print(f"{basicPath} - {problem} kor done - length : {len(stringPart)}")