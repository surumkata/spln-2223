# TPC6

### Informação sobre os ficheiros:
* **corpus.py**: Newspaper Scraper

Neste tpc foi pedido para continuar o scraper de notícias da última aula. Testar com outros sites de notícias (para além do jn), e fazer do programa uma ferramenta automárica períodica.

As funcionalidades manteram-se semelhantes, acrescentando apenas alguns logs de funcionamento.
O Programa foi testado em outros 2 jornais (os dois de angola), o jornal de angola (https://www.jornaldeangola.ao/ao/) e o novo jornal (https://novojornal.co.ao) e os dois funcionaram como o jornal de notícias.
Foi criado uma organização de pastas por dia no programa de modo a que este possa ser usado todos os dias.

Para utilizar o programa de forma periódica, pode se usar a ferramente do unix cron.
Exemplo:
    0 9 * * * python3 '/corpus.py'

    às 9 da manhá todos os dias o programa será corrido