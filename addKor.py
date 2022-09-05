string = """서양에서 개인 작곡가는 음악이 연주되기 오래 전에 음악을 작곡한다. 우리가 듣는 패턴들과 멜로디들은 사전에 계획되고 의도된다. 그러나 일부 아프리카 부족의 음악은 연주자들의 협연의 결과로 즉석에서 생겨난다. 모든 연주자가 어느 한 박자에서 쉴 때의 휴지(休止)이든, 모든 연주가가 함께 연주할 때의 강박(accented beats)이든 간에 들리는 패턴은 계획된 것이 아니라 우연히 얻은 것이다. 전반적인 휴지가 4박자와 13박자에 나타날 때, 그것은 각각의 음악가가 “4박자와 13 박자에 나는 쉴거야.”라고 염두에 두었기 때문이 아니다. 오히려, 모든 연주자의 패턴이 동시에 쉬는 것으로 한데 모아질 때 그것은 무작위로 일어난다. 그 음악가들도 아마 4박자와 13박자에 휴지를 들은 청중만큼 놀란다. 확실히 그 놀라움은 부족의 음악가들이 음악을 연주할 때 경험하는 기쁨 중 하나이다. """

string = ".\n".join(" ".join(string.split("\n")).split(". "))

print(string)

import json

basicPath = r"sources\2020"
problem = 39

string = string.strip()
stringPart = string.split("\n")

with open(f'{basicPath}\{problem}.json', 'r', encoding='UTF8') as f:

    json_data = json.load(f)
for i in range(len(stringPart)):
#    print(stringPart[i])
    json_data["content"][i]["kor"] = stringPart[i]
    


with open(f'{basicPath}\{problem}.json', 'w', encoding='UTF8') as make_file:

    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)



print(f"{basicPath} - {problem} kor done - length : {len(stringPart)}")