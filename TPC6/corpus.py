#!/usr/bin/env python3
import newspaper
import os
import sys
import datetime
import traceback

os.chdir(sys.path[0]) 
path = os.getcwd()

def symlink():
    if not os.path.exists('/tmp/.newspaper_scraper'):
        origem = os.path.join(path,'newspaper_scraper')
        print(origem)
        #os.symlink(origem,'/tmp/.newspaper_scraper/')

def log(log : str, logsFile):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logsFile.write(log + f'[{now}]\n')

def create_dirs():
    #create date dirs
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day

    outFile = f'{path}/articles/{year}/{month}'
    os.makedirs(outFile,exist_ok=True)
    return outFile + f'/{day}.html'

def main():
    symlink()

    url = 'https://www.jn.pt'
    #url = 'https://www.jornaldeangola.ao/ao/'
    #url = 'https://novojornal.co.ao'

    #create log file
    logsFile = open(f'{path}/logs.txt','w')

    log('Geting articles',logsFile)
    
    j = newspaper.build(url,memoized_articles=False)

    nArticles = j.size()
    log(f'{nArticles} articles',logsFile)

    outFile = create_dirs()
    output = open(outFile,'a')

    output.write('<articles>\n')
    
    na = 0
    for article in j.articles:
        log(f'Article {na} of {nArticles}',logsFile)
        na+=1
        try:
            ar = newspaper.Article(article.url())
            ar.download()
            ar.parse()
            output.write(
                f'''
                    <article>
                        <title>
                            {ar.title}
                        </title>
                        <url>
                            {ar.url}
                        </url>
                        <autor>
                            {ar.autor}
                        </autor>
                        <date>
                            {ar.date}
                        </date>
                        <tags>
                            {ar.tags}
                        </tags>
                        <text>
                            {ar.text}
                        </text>
                    </article>
                '''
            )
        except Exception:
            print(traceback.format_exc)
            log(traceback.format_exc,logsFile)

    output.write('</articles>\n')
    output.close()

    log('Finished writing',logsFile)

    logsFile.close()

if __name__ == "__main__":
    main()