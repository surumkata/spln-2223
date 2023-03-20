
# TPC4

### Informação sobre os ficheiros:
* **tokenizador_spln.py**: Tokenizer

Neste tpc foi pedido para finalizar o tokenizer começado na aula. Para tal deviamos concluir algumas tarefas:
- Quebra de pagina
- Separar pontuação das palavras
- Marcar capitulos
- Separar paragrafos de linhas pequenas
- Juntar linhas da mesma frase
- Uma frase por linha
- Tratar Poemas (tagged)

O programa pode ser executado da seguinte maneira:

tokenizador_spln.py [filename de input] [flags] 

### [filename de input] : 

É opcional, por default, o programa lê do stdin.

### [flags] :

- -p : 
Informa que tem poemas marcados, estes serão guardados e imprimidos posteriormente de forma separada

- -o [Filename] :
Atribui um ficheiro de output ao programa (default, o programa imprime para o stdout)