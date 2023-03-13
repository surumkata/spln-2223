import pickle
import ply.yacc as yacc
from medicina_lex import tokens

def p_1(p):
    r'Dict : EntradasC NL'
    p[0] = p[1]

def p_3(p):
    r'EntradasC : EntradasC NL EntradaC'
    p[0] = p[1] + p[3]

def p_4(p):
    r'EntradasC : EntradaC'
    p[0] = p[1]

def p_5(p):
    r'EntradaC : Areas Linguas'
    p[0] = [{
        'areas' : p[1],
        'linguas' : p[2]
    }]

def p_10(p):
    r'Areas : AREAS Text NL'
    p[0] = p[2]

def p_11(p):
    r'Areas : '
    p[0]

def p_12(p):
    r'Text : TEXT'
    p[0] = str(p[1])

def p_13(p):
    r'Text : '
    p[0]

def p_14(p):
    r'Linguas : LANGUAGES NL DictLinguas'
    p[0] = p[3]

def p_15(p):
    r'DictLinguas : DictLinguas DictLingua'
    p[1][p[2][0]] = p[2][1]
    p[0] = p[1]

def p_16(p):
    r'DictLinguas : DictLingua'
    p[0] = { p[1][0] : p[1][1] }

def p_17(p):
    r'DictLingua : LANGUAGE NL DictTermos'
    p[0] = (p[1],p[3])

def p_18(p):
    r'DictTermos : DictTermos DictTermo'
    p[0] = p[1] + p[2]

def p_19(p):
    r'DictTermos : DictTermo'
    p[0] = p[1]

def p_20(p):
    r"DictTermo : '#' TEXT NL Atributos"
    if(p[4] != None):
        p[0] = [{
            'termo' : p[2],
            'atributos' : p[4]
        }]
    else:
        p[0] = [{
            'termo' : p[2]
        }]

def p_21(p):
    r'Atributos : Atributos Atributo'
    if(p[1] != None):
        p[0] = p[1] + [p[2]]
    else: p[0] = [p[2]]

def p_22(p):
    r'Atributos : '
    p[0] = None

def p_23(p):
    r'Atributo : ATRIBUTOS As NL'
    p[0] = p[2]

def p_24(p):
    r'As : As ATRIBUTO'
    p[0] = p[1] + p[2]

def p_25(p):
    r'As : ATRIBUTO'
    p[0] = p[1]



def p_error(p):
    print('Syntax error: ', p)
    parser.error += 1

parser = yacc.yacc()

file = open('medicina.txt','r', encoding='utf-8')
txt = file.read()


parser.entradas = []
parser.error = 0
result = parser.parse(txt)
if parser.error == 0:
    print('No errors in parse')
    print(result[2])
    print(f'Entries : {len(result)}')

    file = open('medicina_bin','wb')
    pickle.dump(result,file)
    file.close()

else:
    print(f'Found {parser.error} errors!')