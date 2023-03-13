import json
import re

file = open('medicina.json', 'r',encoding="utf-8")

dict = json.load(file)

file.close()

file = open('medicina.txt','w',encoding="utf-8")

def listToString(list):
    string = """"""
    for l in list:
        string+= f"{l}, "
    return string[:-2]


def valid_entry(entry,type):
    if type == "completas":
        return ("areas" in entry and "traducoes" in entry and not_empty(entry["areas"]) and not_empty(entry["traducoes"]))
    elif type == "remissivas":
        return ("areas" in entry and "vids" in entry and not_empty(entry['areas']) and not_empty(entry["vids"]))
    else: return False

def valid_lingua(termos):
    if(not_empty(termos)):
        for dictTermo in termos:
            if('termo' in dictTermo and dictTermo['termo'] != ""):
                pass
            else: 
                return False
    else: return False
        
    return True

def not_empty(list):
    return len(list) > 0

typeTranslate = {
    "completas" : "Completes",
    "remissivas" : "Cross"
}

generos = ["m","f","a"]

for type in dict:
    file.write(f"{typeTranslate[type]} entries:\n")
    for index in dict[type]:
        entry = dict[type][index]
        if valid_entry(entry, type):
            file.write(f"    Index: {index}\n")
            if("areas" in entry and len(entry['areas']) > 0):
                file.write(f"    Areas: {listToString(entry['areas'])}\n")
            if("traducoes" in entry):
                file.write(f"    Languages:\n")
                traducoes = entry['traducoes']
                for lingua in traducoes:
                    termos = traducoes[lingua]
                    if(valid_lingua(termos)):
                        file.write(f"                {lingua.upper()}:\n")
                    for termo in termos:
                        if('termo' in termo and termo['termo'] != ""):
                            t = termo['termo']
                            exp = re.compile(r"([\w\s]+)(((\[\w+\.\])\s*)*)")
                            groups = exp.findall(t)
                            if(groups != None and len(groups) > 0):
                                t = groups[0][0]
                                atributos = groups[0][1]
                                file.write(f"                   # {t}\n")
                                if(atributos != ""):
                                    file.write(f"                       >> {atributos}\n")
                            elif (t != ""):
                                file.write(f"                   # {t}\n")
                            if('nota' in termo):
                                nota = termo['nota']
                                if (nota != ""): 
                                    file.write(f"                       Note: {nota}\n")
                            if('genero' in termo):
                                genero = termo['genero']
                                if(genero != ""):
                                    if(genero in generos): 
                                        file.write(f"                       Gender: {genero.capitalize()}\n")
                    if(lingua == "gl" and t != ""):
                        if(len(entry['sinonimos']) > 0 and listToString(entry['sinonimos']) != ""):
                            sinonimos = listToString(entry['sinonimos'])
                            if(sinonimos != ""): 
                                file.write(f"                       Synonyms: {sinonimos}\n")
                        if(len(entry['variacoes']) > 0 and listToString(entry['variacoes']) != ""):
                            variacoes = listToString(entry['variacoes'])
                            if(variacoes != ""): 
                                file.write(f"                       Variations: {variacoes}\n")
            if("vids" in entry and len(entry['vids']) > 0):
                file.write(f"       Vids:{listToString(entry['vids'])}\n")
            file.write("\n")


file.close()