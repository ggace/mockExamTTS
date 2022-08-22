string = """Without guidance from their teacher, students will not embark on a
journey of personal development that recognizes the value of
cooperation. Left to their own devices, they will instinctively become
increasingly competitive with each other. They will compare scores,
reports, and feedback within the classroom environment ― just as they
do in the sporting arena. We don’t need to teach our students about
winners and losers. The playground and the media do that for them.
However, we do need to teach them that there is more to life than
winning and about the skills they need for successful cooperation. A
group working together successfully requires individuals with a multitude
of social skills, as well as a high level of interpersonal awareness. While
some students inherently bring a natural understanding of these skills
with them, they are always in the minority. To bring cooperation
between peers into your classroom, you need to teach these skills
consciously and carefully, and nurture them continuously throughout the
school years.
"""

string = ".\n".join(" ".join(string.split("\n")).split(". "))

import json

basicPath = r"sources\2021"
problem = 20

string = string.strip()
stringPart = string.split("\n")
tempList = []

for string in stringPart:
    tempList.append({"eng" : string, "kor" : ""})

tempList = json.dumps(tempList)

f = open(rf'{basicPath}\{problem}.json', 'w', encoding='UTF8')
f.write("{")
f.write("\n")
f.write(f"\t\"topic\" : \"\", ")
f.write("\n")
f.write('\t"topicEng": "",\n')
f.write(f"\t\"content\" : {tempList}")
f.write("\n")
f.write("}")

f.close()

print(f"{basicPath} - {problem} done - length : {len(stringPart)}")