
import json
def extract_route(string):
    lista= string.split()
    string_i=lista[1]
    rota= string_i[1:]
    return rota



def read_file(file_path):
    with open(file_path,'rb') as arquivo:
        leitura= arquivo.read()
    return leitura

def load_data(file_name):

    # Abre o arquivo JSON e carrega o conteúdo como um objeto Python
    with open( "data/"+ file_name, 'r') as file:
        # esse metodo loads pega o que tinha no arquivo json  e transforma em um objeto python
        content= file.read()
        data = json.loads(content)
    
    return data

def load_template(file_name):
    with open("templates/" + file_name, 'r') as file:
        template = file.read()
    return template


