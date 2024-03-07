line = input("%") # ler do stdin
sum = 0 # guardar o valor de output

aux = "" # string auxiliar para guardar valores com mais que um digito

state = True
aux_state = "" # string auxiliar para guardar as key-word "on" e "off" para a transição de estado

for c in line:
    c = c.upper() # case insesitive

    if state == True: # se o somador estiver ligado ignora todos os caracteres, construindo uma string que representa o número inteiro lido até ao momento e guarda-o na soma
        if '0' <= c <= '9':
            aux += c
        else:
            if len(aux) != 0:
                sum += int(aux)
                aux = ""

    if c == "O": # guardar os estados e fazer as transições
        aux_state = c
    elif c == "N" and aux_state == "O": 
        state = True
        aux_state = ""
    elif c == "F" and aux_state == "OF":
        state = False
        aux_state = ""
    elif c == "F" and aux_state == "O":
        aux_state += c
    elif c == "=":
        print(sum)
        


























import sys
import ply.lex as lex

# Lista de comandos SQL
commands = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'in' : 'IN',
    'and': 'AND',
    'or': 'OR',
    'create' : 'CREATE',
    'drop' : 'DROP',
    'show' : 'SHOW',
    'use' : 'USE',
    'alter' : 'ALTER',
    'grant' : 'GRANT',
    'revoke' : 'REVOKE',
    'union' : 'UNION',
    'group by' : 'GROUP_BY',
    'order by' : 'ORDER_BY',
    'outer join': 'OUTER_JOIN',
    'inner join': 'INNER_JOIN',
    'left join' : 'LEFT_JOIN',
    'right join' : 'RIGHT_JOIN',
    'full join' : 'FULL_JOIN'
}

# Lista dos tokens
tokens = (
    "COMMAND",
    "ATTRIBUTE",
    "DELIMITER",
    "NUMBER",
    "OPERATOR",
    "ENDCMD",
) + tuple(commands.values())

# Expressões regulares e funções para cada token

# Tem que ficar por cima do comando porque se não capta os números como atributos
def t_NUMBER(token): 
    r"\d+(\.\d+)?"
    if '.' in token.value:
        float(token.value)
    else: 
        int(token.value)
        
    return token

def t_COMMAND(token):
    r"\b\w+(\s+(?i:by|join))?\b"
    token_val = token.value.lower()
    if token_val in commands:
        token.type = commands[token_val]
    else:
        token.type = "ATTRIBUTE"
        
    return token

t_DELIMITER = r","


def t_OPERATOR(token):
    r"\+|-|\*|>=|<=|>|<|="
    return token

t_ENDCMD = r";"

# Manter a contagem das linhas
def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

# Ignoras whitespaces
t_ignore  = ' \t\n'

# Error (skip do caracter)
def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)

lexer = lex.lex()

while True:
    line = input("\nDigite uma linha (Ctrl+C para sair):\n")

    # inserir a linha no lexer
    lexer.input(line)

    for token in lexer:
        print(token)
        
