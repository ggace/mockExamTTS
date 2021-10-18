import json

string = """James Walker was a renowned wrestler and he made his living through wrestling. 
In his town, there was a tradition in which the leader of the town chose a day when James demonstrated his skills. 
The leader announced one day that James would exhibit his skills as a wrestler and asked the people if there was anyone to challenge him for the prize money.
Everyone was looking around in the crowd when an old man stood up and said with a shaking voice, “I will enter the contest against him.” 
Everyone burst out laughing thinking that it was a joke. 
James would crush him in a minute. 
According to the law, the leader could not stop someone who of his own free will entered the competition, so he allowed the old man to challenge the wrestler.
When James saw the old man, he was speechless. 
Like everyone else, he thought that the old man had a death wish. 
The old man asked James to come closer since he wanted to say something to him. 
James moved closer and the old man whispered, “I know it is impossible for me to win but my children are starving at home. Can you lose this competition to me so I can feed them with the prize money?”
James thought he had an excellent opportunity to help a man in distress. 
He did a couple of moves so that no one would suspect that the competition was fixed. 
However, he did not use his full strength and allowed the old man to win. 
The old man was overjoyed when he received the prize money. 
That night James felt the most victorious he had ever felt."""

basicPath = r"sources\2020"
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
