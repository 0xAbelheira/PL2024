import sys
import re

def conversor(line):
    global f_nl
    # um heading é todo o texto que vem depois de um ou mais '#' (com pelo menos um espaço entre eles, até 6 níveis de heading)
    re_heading = r"^(#{1,6})\s(.*)" 
    # um bold é todo o texto entre '**' ou '__' tendo em conta que não pode haver espaços a separar estes simbolos do inicio e do fim da string
    re_bold = r"(\*\*|__)([^ ].*[^ ])\1"
    # o itálico é idêntico ao bold mas com apenas um asterisco ou um underscore ('*' ou '_')
    re_it = r"(\*|_)([^ ].*[^ ])\1"
    # uma lista numerada é um digito e um ponto final, seguido com qualquer texto e separados por um espaço (sem esquecer que pode haver múltiplos espaços entre itens)
    re_nl = r"^\d\. (.+)$"
    # um link é texto (obrigatório) entre '[' ']' seguido do url em questão entre '(' ')'
    re_link = r"\[([^\]]+(?:\[[^\]]*\][^\]]*)*)\]\(([^)]+)\)"
    # uma imagem é idêntica ao link só que com um '!' no início da string (a legenda é opcional, mas os '[' ']' são obrigatórios)
    re_img = r"!\[([^\]]*(?:\[[^\]]*\][^\]]*)*)\]\(([^)]+)\)"
    
    """ notas: 
    a responsabilidade de inserir um link e uma path de imagem válidos são do utilizador
    usou-se grupos de não captura para detetar padrões de pares de '[' ']' e de '(' ')' dentro dos textos dos links e das imagens
    """
    
    match = re.match(re_heading, line)
    if match:
        line = re.sub(re_heading, f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>", line)

    match = re.search(re_bold, line) # o bold tem de ser detetado antes do italico
    if match:
        line = re.sub(re_bold, f"<b>{match.group(2)}</b>", line)

    match = re.search(re_it, line)
    if match:
        line = re.sub(re_it, f"<i>{match.group(2)}</i>", line)
        
    match = re.match(re_nl, line) # 
    if match:
        if not f_nl: # flag começa a False para sabermos que é o primeiro elemento da lista
            line = re.sub(re_nl, f"<ol><li>{match.group(1)}</li>", line)
            f_nl = True
        else:
            line = re.sub(re_nl, f"<li>{match.group(1)}</li>", line)
    elif f_nl: # se o estado da flag for True e não der match, sabemos que se trata do último elemento da lista
        line = f"</ol>{line}" # fechar uma lista numerada. Caso esta esteja no final do ficheiro a condição não vai ser verificada e por isso a lista é fechada na main
        f_nl = False
        

    match = re.search(re_img, line) # os links tem que ser detetados antes das imagens
    if match:
        line = re.sub(re_img, f'<img src="{match.group(2)}" alt="{match.group(1)}"/>', line)
        
    match = re.search(re_link, line)
    if match:
        line = re.sub(re_link, f'<a href="{match.group(2)}">{match.group(1)}</a>', line)


    return line
    
def main():
    input_path = sys.argv[1] # ler a path do ficheiro de input

    output_file = ["<html>","<body>"] # inicio de um file html
    
    with open(input_path, 'r') as f: # leitura do ficheiro MD
        lines = f.readlines()
        for line in lines:
            output_file.append(conversor(line)) # criação da estrutura para converter para html
    
    if f_nl: # flag para fechar uma lista numerada que apareça no final do ficheiro
        output_file.append("</ol>")
        
    output_file.append("</body>") # fechar as tags para formar um file html correto
    output_file.append("</html>")
    
    with open('output.html', 'w') as f: # criar ficheiro output
        f.writelines(output_file)
    print("File Successfully Converted to output.html !!")
        
if __name__ == "__main__":
    f_nl = False
    main()
        
        
        