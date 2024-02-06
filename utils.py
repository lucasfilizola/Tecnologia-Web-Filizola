def extract_route(string):
    lista= string.split()
    string_i=lista[1]
    rota= string_i[1:]
    return rota



def read_file(file_path):
    with open(file_path,'rb') as arquivo:
        leitura= arquivo.read()
    return leitura