#!/usr/bin/env python
import argparse
from glob import glob
from gensim.models import Word2Vec
from gensim.utils import tokenize


parser = argparse.ArgumentParser(
    prog="Criar Modelo",
    epilog="Made for SPLN 2022/2023"    
)

parser.add_argument('dir')
parser.add_argument('-e','--epochs',default=25)
parser.add_argument('-d','--dimension',default=300)
parser.add_argument('-o','--output',default='modelo')

args = parser.parse_args()
dir = args.dir
files = glob(f'{dir}/*.txt')

epochs = args.epochs
dim = args.dimension
out = args.output


cont = []
for file in files:
    f = open(file,'r',encoding="utf8")
    for line in f:
        cont.append(list(tokenize(line,lower=True)))

model = Word2Vec(cont,epochs=epochs, vector_size=dim)

model.save(f'{out}.vec')