
# TPC3

### Informação sobre os ficheiros:
* **medicina_lex.py**: lexer da gramática
* **medicina.yacc.py**: parser da gramática
* **medicina.txt**: ficheiro com a informação numa representação mais acessivel ao olho humano. É este ficheiro que será parsed para ser transformado numa nova "view"
* **lexer.txt**: ficheiro resultante de passar o lexer no ficheiro medicina.txt (utilizado de debug durante o desenvolvimento deste tpc)
* **medicina_bin**: ficheiro com o binario da estrutura em python resultante de passar o parser no ficheiro medicina.txt
* **generate_html.py**: ficheiro que gera o html da nova visualização da estrutura de dados apartir do medicina_bin
* **dicionario.html**: ficheiro html com a nova visualização pretendida

Neste tpc foi pedido para fazer uma gramática à nossa escolha de uma visualização predefenida por nós no tpc anterior, e com isso gerar uma estrutura de dados para que se pudesse posteriormente gerar novas visualizaçãos (pdf,html,etc).

