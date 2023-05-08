#!/usr/bin/env python
import argparse
from glob import glob
from gensim.models import Word2Vec
from gensim.utils import tokenize
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
    prog="Criar Modelo",
    epilog="Made for SPLN 2022/2023"    
)

parser.add_argument('dir')
parser.add_argument('-e','--epochs',default=25)
parser.add_argument('-d','--dimension',default=300)
parser.add_argument('-o','--output',default='modelo')
parser.add_argument('-html',default=False,action='store_true')

args = parser.parse_args()
dir = args.dir
html = args.html
if(not html): 
    files = glob(f'{dir}/*.txt')
else: 
    files = glob(f'{dir}/*.html',recursive=True)

epochs = args.epochs
dim = args.dimension
out = args.output


cont = []
if(not html):
    for file in files:
        f = open(file,'r',encoding="utf8")
        for line in f:
            cont.append(list(tokenize(line,lower=True)))
        f.close()
else:
    for file in files:
        f = open(file,'r',encoding="utf8")
        html = f.read()
        soup = BeautifulSoup(html,features='lxml')
        for elem in soup.find_all('text'):
            text = elem.get_text()
            for line in text.splitlines():
                cont.append(list(tokenize(line,lowercase=True)))
        f.close()

model = Word2Vec(cont,epochs=epochs, vector_size=dim)

model.save(f'{out}.vec')