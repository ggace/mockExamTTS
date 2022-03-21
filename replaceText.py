string = """Some beginning researchers mistakenly believe that a good hypothesis is one that is guaranteed to be right (e.g., alcohol will slow down reaction time).
However, if we already know your hypothesis is true before you test  it,  testing your hypothesis won’t tell us anything new.
Remember, research is supposed to produce new knowledge.
To get new knowledge, you, as a researcher­explorer, need to leave the safety of the shore (established facts) and venture into uncharted waters (as Einstein said, “If we knew what we were doing, it would not be called research, would it?”).
If your predictions about what will happen in these uncharted waters are wrong, that’s okay:
Scientists are allowed to make mistakes (as Bates said, “Research is the process of going up alleys to see if they are blind”).
Indeed, scientists often learn more from predictions that do not turn out than from those that do."""

import json

basicPath = r"sources\2021"
problem = 24

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
