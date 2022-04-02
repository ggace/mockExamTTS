string = """Of all the medical achievements of the 1960s, the most widely known was the first heart transplant, performed by the South African surgeon Christiaan Barnard in 1967. 
The patient’s death 18 days later did not weaken the spirits of those who welcomed a new era of medicine. 
The ability to perform heart transplants was linked to the development of respirators, which had been introduced to hospitals in the 1950s. 
Respirators could save many lives, but not all those whose hearts kept beating ever recovered any other significant functions. 
In some cases, their brains had ceased to function altogether. 
The realization that such patients could be a source of organs for transplantation led to the setting up of the Harvard Brain Death Committee, and to its recommendation that the absence of all “discernible central nervous system activity” should be “a new criterion for death”.
The recommendation has since been adopted, with some modifications, almost everywhere. """

import json

basicPath = r"sources\2020"
problem = 39

string = string.strip()
stringPart = string.split("\n")
tempList = []

for string in stringPart:
    tempList.append({"eng" : string, "kor" : ""})
print(tempList)

tempList = json.dumps(tempList)

f = open(rf'{basicPath}\{problem}.json', 'w', encoding='UTF8')
f.write("{")
f.write("\n")
f.write(f"\"topic\" : \"\", ")
f.write("\n")
f.write(f"\"content\" : {tempList}")
f.write("\n")
f.write("}")

f.close()
