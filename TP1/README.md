
# TPC1

Extração informações do ficheiro *medicina.pdf* e estruturação para outro formato de dados.

### Informação sobre os ficheiros:
* **medicina.pdf**: pdf sobre o vocabulário de medicina (galego-espanhol-inglés-portugués);
* **medicina.xml**: xml gerado sobre o ficheiro **medicina.pdf** com o comando:
	*  *pdftohtml medicina.pdf -xml -f 20 -l 543* (descartamos as páginas que não nos interessavam);
* **medicina_marcado.txt**: ficheiro resultante de fazer as marcações no xml, apenas uma representação intermediária para estudo e desenvolvimento do script. 
* **medicina.json**: ficheiro json com a informação final guardada;
* **medicina.py**: script em Python.

Tendo na aula já feito algumas marcações e retirado o footer e o header, utilizei das mesmas ideias para fazer outras marcações no ficheiro medicina.xml (marcações de linguas, sinonimos, áreas, etc). 
Enquanto fazia as marcações, guardei sempre no medicina_marcado.txt a versão marcada para caso de estudo se estava o trabalho das marcações estava a correr bem.
No fim das marcações, percorria o resultado fazendo split através das marcações feitas, para separar num dicionário em Python.
Por fim guardei esse dicionário no ficheiro medicina.json.

Resumindo o trabalho feito:
    -> Marcação do xml
    -> Processamento dessa marcação numa estrutura de dados
    -> Gravação dessa estrutura de dados num ficheiro