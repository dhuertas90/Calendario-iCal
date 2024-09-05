import pickle

def desarchivar(texto):
    with open(texto, 'rb') as f:
        lista = pickle.load(f)
    return lista

def archivar(lista, texto):
    with open(texto, 'wb') as f:
        pickle.dump(lista, f)
