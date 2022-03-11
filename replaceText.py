string = """Psychological research has shown that people naturally divide up cognitive labor, often without thinking about it.
Imagine you’re cooking up a special dinner with a friend.
You’re a great cook, but your friend is the wine expert, an amateur sommelier.
A neighbor drops by and starts telling you both about the terrific new wines being sold at the liquor store just down the street.
There are many new wines, so there’s a lot to remember.
How hard are you going to try to remember what the neighbor has to say about which wines to buy?
Why bother when the information would be better retained by the wine expert sitting next to you?
If your friend wasn’t around, you might try harder.
After all, it would be good to know what a good wine would be for the evening’s festivities.
But your friend, the wine expert, is likely to remember the information without even trying."""

import json

basicPath = r"sources\2021"
problem = 33

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
