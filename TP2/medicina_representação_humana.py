import json

file = open('medicina.json', 'r')

dict = json.load(file)

file.close()

file = open('medicina.txt','w')

def listToString(list):
    string = """"""
    for l in list:
        string+= f"{l}, "
    return string[:-2]

for type in dict:
    file.write(f"#{type.capitalize()}:\n")
    for entry in dict[type]:
        entry = dict[type][entry]
        if("areas" in entry and len(entry['areas']) > 0):
            file.write(f"    Area(s): {listToString(entry['areas'])}\n")
        if("traducoes" in entry):
            file.write(f"    Traducoes(s):\n")
            traducoes = entry['traducoes']
            for lingua in traducoes:
                file.write(f"       {lingua.capitalize()}:\n")
                lingua = traducoes[lingua]
                for termo in lingua:
                    if('termo' in termo):
                        termo = termo['termo']
                        file.write(f"           - {termo}\n")
        if("nome" in entry):
            file.write(f"   - {entry['nome']}\n")
        if("vids" in entry):
            file.write(f"   Vids:{entry['vids']}\n")
        file.write("\n")


file.close()