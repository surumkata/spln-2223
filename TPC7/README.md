# TPC7

### Informação sobre os ficheiros:
* **cria_modelo.py**: Programa que cria o modelo
* **test.py**: Programa que testa o modelo com analogias

Neste tpc foi pedido para continuar fazer um programa semalhante ao da aula so que com os jornais do tpc6 invês dos livros do Harry Potter.
Os ficheiros e funcionalidades seguem semelhantes aos feitos na aula.

Nos testes de analogias, o programa lê de um .txt e testa linha a linha.
É possível fazer 3 opções de testes:

    -> Se oferecido 3 palavras separadas por espaços (ex. "Portugal Europa Brasil"), então o programa vai devolver a analogia feita usando essas 3 palavras, (as 2 primeiras como positivo e a terceira como negativa);
    
    -> Se oferecido 4 palavras separadas por espaços (ex. "Portugal Europa Brasil América"), então o programa vai fazer a mesma analogia como no teste anterior, e vai verificar se a quarta palavra dada é igual à palavra gerada na analogia, devolvendo true ou false.

    -> Se oferecido 3 palavras, 2 delas separadas por barra (ex. "Portugal Europa|América"), então o programa vai verificar se a primeira palavra é mais similiar com a segunda ou com a terceira.