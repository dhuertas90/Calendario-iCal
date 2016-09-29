import pickle


def desarchivar(texto):
    f = open(texto,'r')
    lista = pickle.load(f)
    f.close()
    return lista

def archivar(lista, texto):
    f = open(texto, 'w')
    pickle.dump(lista, f)
    f.close()


