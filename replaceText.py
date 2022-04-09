string = """Hubert Cecil Booth is often credited with inventing the first powered mobile vacuum cleaner.
In fact, he only claimed to be the first to coin the term “vacuum cleaner” for devices of this nature, which may explain why he is so credited.
As we all know, the term “vacuum” is an inappropriate name, because there exists no vacuum in a vacuum cleaner.
Rather, it is the air moving through a small hole into a closed container, as a result of air being blown out of the container by a fan on the inside.
But I suppose a “rapid air movement in a closed container to create suction” cleaner would not sound as scientific or be as handy a name.
Anyway, we are stuck with it historically, and it is hard to find any references to “vacuum” prior to Booth.
Interestingly, Booth himself did not use the term “vacuum” when he filed a provisional specification describing in general terms his intended invention."""

import json

basicPath = r"sources\2019"
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
f.write(f"\t\"topic\" : \"\", ")
f.write("\n")
f.write('"topicEng": "",')
f.write(f"\t\"content\" : {tempList}")
f.write("\n")
f.write("}")

f.close()
