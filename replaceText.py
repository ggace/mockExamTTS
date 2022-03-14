string = """At the University of Iowa, students were briefly shown numbers that they had to memorize.
Then they were offered the choice of either a fruit salad or a chocolate cake.
When the number the students memorized was seven digits long, 63% of them chose the cake.
When the number they were asked to remember had just two digits, however, 59% opted for the fruit salad.
Our reflective brains know that the fruit salad is better for our health, but our reflexive brains desire that soft, fattening chocolate cake.
If the reflective brain is busy figuring something else out ― like trying to remember a seven­digit number ― then impulse can easily win.
On  the  other  hand,  if  we’re  not  thinking  too  hard  about  something  else  (with  only  a  minor distraction like memorizing two digits), then the reflective system can deny the emotional impulse of the reflexive side."""

import json

basicPath = r"sources\2021"
problem = 40

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
