string = """A long time ago, a farmer in a small town had a neighbor who was a hunter. 
The hunter owned a few fierce and poorly-trained hunting dogs. 
They jumped the fence frequently and chased the farmer’s lambs. 
The farmer asked his neighbor to keep his dogs in check, but his words fell on deaf ears. 
One day when the dogs jumped the fence, they attacked and severely injured several of the lambs. 
The farmer had had enough by this point. 
He went to the nearest city to consult a judge. 
After listening carefully to his story, the judge said, “I could punish the hunter and instruct him to keep his dogs chained or lock them up. But you would lose a friend and gain an enemy. Which would you rather have for a neighbor, a friend or an enemy?”
The farmer replied that he preferred a friend. 
“All right, I will offer you a solution that keeps your lambs safe and will also turn your neighbor into a good friend.” 
Having heard the judge’s solution, the farmer agreed. 
As soon as the farmer reached home, he immediately put the judge’s suggestions to the test.
He selected three of the cutest lambs from his farm. 
He then presented them to his neighbor’s three small sons. 
The children accepted with joy and began to play with them. 
To protect his sons’ newly acquired playmates, the hunter built a strong doghouse for his dogs. 
The dogs never bothered the farmer’s lambs again. 
Out of gratitude for the farmer’s generosity toward his children, the hunter often invited the farmer for feasts. 
In turn, the farmer offered him lamb meat and cheese he had made. 
The farmer quickly developed a strong friendship with him."""

import json

basicPath = r"sources\2019"
problem = 43

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
