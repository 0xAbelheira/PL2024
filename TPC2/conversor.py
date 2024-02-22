import sys
import re

def conversor(line):
    # um heading é todo o texto que vem depois de um ou mais '#' (com pelo menos um espaço entre eles, até 6 níveis de heading)
    re_heading = r"^(#+)\s(.*)" 
    # um bold é todo o texto entre '**' ou '__' tendo em conta que não pode haver espaços a separar estes simbolos do inicio e do fim da string
    re_bold = r"(\*\*|__)([^ ])(.*)\2\1"
    # o itálico é idêntico ao bold mas com apenas um asterisco ou um underscore ('*' ou '_')
    re_it = r"(\*|__)([^ ])(.*)\2\1"
    re_nl =
    re_link =
    re_img =

def main():
    input_path = sys.argv[1] # ler a path do ficheiro de input
    print(input_path)
    
    output_file = ["<html>","<body>"] # inicio de um file html
    
    with open(input_path, 'r') as f: # leitura do ficheiro MD
        lines = f.readlines()
        for line in lines:
            output_file.append(conversor(line)) # criação da estrutura para converter para html
    
    output_file.append("</body>") # fechar as tags para formar um file html correto
    output_file.append("</html>")
    
    with open('output.html', 'w') as f: # criar ficheiro output
        f.writelines(output_file)
        
        
        
        
        