string = """국제연합은 모든 기업들이 인공위성의 임무 종료 후 25년 이내에 위성을 궤도에서 제거해 줄 것을 요청하고 있다. 하지만 인공위성이 작동하지 않을 수 있기(그리고 종종 작동하지 않기) 때문에 이것은 시행하기에 까다롭다. 이 문제를 해결하기 위해 전세계의 몇몇 회사들이 새로운 해결책을 내놓았다. 이것은 수명이 다한 인공위성을 궤도에서 제거하고, 대기권으로 다시 끌어들이는 것을 포함하는데, 거기에서 그것은 다 타 버리게 될 것이다. 우리가 이것을 할 수 있는 방법은 위성이 궤도에서 떨어져
나오도록 대기 항력을 증가시키면서 작살을 이용해서 위성을 잡거나, 거대한 그물로 그것을 잡거나, 자석을 이용하여 위성을 잡거나, 레이저를 발사하여 위성을 가열하는 것을 포함한다. 하지만, 이러한 방법은 지구 궤도를 도는 큰 위성들에게만 유용하다. 우리가 페인트 조각이나 금속 같은
작은 잔해물을 집어들 수 있는 방법은 정말로 없다. 우리는 그것들이 자연적으로 지구의 대기로
다시 들어오기를 기다려야 할 뿐이다. 
"""

string = ".\n".join(" ".join(string.split("\n")).split(". "))

import json

basicPath = r"sources\2021"
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