string = """In the West, an individual composer writes the music long before it is performed. The patterns and melodies we hear are pre-planned and intended. Some African tribal music, however, results from collaboration by the players on the spur of the moment. The patterns heard, whether they are the silences when all players rest on a beat or the accented beats when all play together, are not planned but serendipitous. When an overall silence appears on beats 4 and 13, it is not because each musician is thinking, “On beats 4 and 13, I will rest.” Rather, it occurs randomly as the patterns of all the players converge upon a simultaneous rest. The musicians are probably as surprised as their listeners to hear the silences at beats 4 and 13. Surely that surprise is one of the joys tribal musicians experience in making their music."""

string = ".\n".join(" ".join(string.split("\n")).split(". "))
print(string)
import json

basicPath = r"sources\2020"
problem = 39

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