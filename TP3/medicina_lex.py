import ply.lex as lex


tokens = ('AREAS','LANGUAGES','LANGUAGE','ATRIBUTOS','NL','TEXT','ATRIBUTO')

literals = [':','#','+','(',')']

t_ANY_ignore =" *"

def t_AREAS(t):
    r'Areas:'
    return t

def t_LANGUAGES(t):
    r'Languages:'
    return t

def t_LANGUAGE(t):
    r'(EN:|PT:|LA:|GL:|ES:)'
    return t

def t_ATRIBUTOS(t):
    r'>>'
    return t

def t_NL(t):
    r'\n'
    return t

def t_TEXT(t):
    r'\w[^\:>#\n]*'
    return t

def t_ATRIBUTO(t):
    r'\[\w+\.\]'
    return t

def t_error(t):
    print('Ilegal character "%s"' % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
file = open('medicina.txt','r', encoding='utf-8')
txt = file.read()
file.close()
file = open('lexer.txt','w+')

lexer.input(txt)
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     file.write(f'{tok}\n')
file.close()

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)