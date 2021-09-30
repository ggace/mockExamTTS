string = """Nancy Lowry and David Johnson conducted an experiment to study a teaching environment where fifth and sixth graders were assigned to interact on a topic. 
With one group, the discussion was led in a way that built an agreement. 
With the second group, the discussion was designed to produce disagreements about the right answer. 
Students who easily reached an agreement were less interested in the topic, studied less, and were less likely to visit the library to get additional information. 
The most noticeable difference, though, was revealed when teachers showed a special film about the discussion topic — during lunch time! 
Only 18 percent of the agreement group missed lunch time to see the film, but 45 percent of the students from the disagreement group stayed for the film. 
The thirst to fill a knowledge gap — to find out who was right within the group — can be more powerful than the thirst for slides and jungle gyms. """

basicPath = r"sources\2021"
problem = 40

string = string.strip()
string = string.replace("\n", " ")
print(string)

f = open(rf'{basicPath}\{problem}.json', 'w', encoding='UTF8')
f.write("{")
f.write("\n")
f.write(f"\"topic\" : \"\", ")
f.write("\n")
f.write(f"\"content\" : \"{string}\"")
f.write("\n")
f.write("}")

f.close()
