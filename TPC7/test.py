import argparse
from gensim.models import Word2Vec

parser = argparse.ArgumentParser(
    prog="Teste",
    epilog="Made for SPLN 2022/2023"    
)

parser.add_argument('model')
parser.add_argument('--analogias','-a',default='teste.txt')

args = parser.parse_args()

file_model = args.model
analogias = args.analogias



model = Word2Vec.load(file_model)

f = open(analogias,'r',encoding="utf8")
i = 0
for line in f:
    i+=1
    line = line.strip()
    words = line.split(" ")
    dim = len(words)
    if dim >= 3:
        res = model.wv.most_similar(positive=[words[0],words[1]],negative=[words[2]])
        res = res[0][0]
        if dim == 3:
            print(f'Teste Analogia {i}: {res}')
        elif dim == 4:
            print(f'Teste Validação {i}: ({res == words[3]},{res})')
    elif dim == 2:
        escolhas = words[1].split("|")
        if len(escolhas) == 2:
            e1 = model.wv.n_similarity([words[0]],[escolhas[0]])
            e2 = model.wv.n_similarity([words[0]],[escolhas[1]])
            escolha = escolhas[1]
            if(e1 > e2):
                escolha = escolhas[0]
            print(f'Teste Escolha {i}: {escolha}')