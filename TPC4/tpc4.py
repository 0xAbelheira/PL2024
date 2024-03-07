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