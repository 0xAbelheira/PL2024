import ply.lex as lex
import sys
import json
from datetime import datetime

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'ADD',
    'REMOVE',
    'UPDATE',
    'HELP'
)

t_LISTAR = r'\bLISTAR\b'

def t_SELECIONAR(t):
    r'\bSELECIONAR\b\s+[A-Z0-9]+'
    return t

def t_MOEDA(t):
    r'\bMOEDA\b\s+.*'
    return t

def t_SAIR(t):
    r'\bSAIR\b'
    return t

def t_ADD(t):
    r'\bADD\b'
    return t

def t_REMOVE(t):
    r'\bREMOVE\b\s+[A-Z0-9]+'
    return t

def t_UPDATE(t):
    r'\bUPDATE\b'
    return t

def t_HELP(t):
    r'\bHELP\b'
    return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
t_ignore = ' \t\n'

lexer = lex.lex()

saldo = 0
stock = []

def load_stock(fname):
    try:
        with open(fname, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_stock(stock, fname):
    with open(fname, 'w') as f:
        json.dump(stock, f, indent=4)

def add_produto(stock):
    codigo = input("maq: Qual o código do produto que deseja adicionar?: ")
    if codigo in stock:
        quantity = int(input("maq: Que quantidade deseja adicionar?: "))
        stock[codigo]["quantidade"] += quantity
        print("maq: Stock atualizado com sucesso.")
    else:
        name = input("maq: Qual o nome do produto que deseja adicionar?: ")
        quantity = int(input("maq: Que quantidade deseja adicionar?: "))
        price = float(input("maq: Qual o preço do produto?: "))
        stock[codigo] = {
            "nome_produto": name,
            "quantidade": quantity,
            "preco": price
        }
        print("maq: Novo produto adicionado com sucesso.")

def remover_produto(stock, codigo):
    if codigo in stock:
        del stock[codigo]
        print("maq: Produto removido com sucesso.")
    else:
        print("maq: Produto não encontrado.")

def update(stock):
    codigo = input("maq: Qual o código do produto que deseja alterar?: ")
    if codigo in stock:
        name = input("maq: Qual o novo nome do produto?: ")
        stock[codigo]["nome_produto"] = name
        quantity = int(input("maq: Que quantidade existe de momento?: "))
        stock[codigo]["quantidade"] = quantity
        price = float(input("maq: Qual o novo preço do produto?: "))
        stock[codigo]["preco"] = price
        print("maq: Produto atualizado com sucesso.")
    else:
        print("maq: Produto não encontrado.")

def help():
    print("maq: Comandos disponíveis:")
    print("- LISTAR: Lista todos os produtos no stock.")
    print("- MOEDA <valor>: Adiciona moedas ao saldo da máquina. Exemplo: MOEDA 1E, 50C")
    print("- SELECIONAR <código>: Seleciona um produto para compra. Exemplo: SELECIONAR ABC123")
    print("- ADD: Adiciona um novo produto ao stock.")
    print("- REMOVE <código>: Remove um produto do estoque. Exemplo: REMOVE ABC123")
    print("- UPDATE: Atualiza as informações de um produto no estoque.")
    print("- HELP: Mostra esta mensagem de ajuda.")
    print("- SAIR: Sai da aplicação.")

def listar_stock(stock):
    header = "cod | nome | quantidade |  preço"
    print(header)
    print("-" * len(header))
    
    for codigo, produto in stock.items():
        nome_produto = produto['nome_produto']
        quantidade = produto['quantidade']
        preco = produto['preco']
        linha = f"{codigo} | {nome_produto} | {quantidade} | {preco:.2f}"
        print(linha)

def comprar_produto(stock, saldo, codigo):
    if codigo in stock and stock[codigo]["quantidade"] != 0:
        preco = stock[codigo]["preco"] * 100
        if saldo >= preco:
            saldo -= preco
            stock[codigo]["quantidade"] -= 1
            print(f"maq: Pode retirar o produto dispensado \"{stock[codigo]['nome_produto']}\".")
            saldo_euros = saldo // 100
            saldo_centavos = saldo % 100
            print(f"maq: Saldo = {saldo_euros}e {saldo_centavos}c .")
            save_stock(stock, "stock.json")
            return stock, saldo
        else:
            print(f"maq: Saldo insuficiente para satisfazer o seu pedido.")
            saldo_euros = saldo // 100
            saldo_centavos = saldo % 100
            preco_euros = preco // 100
            preco_centavos = preco % 100
            print(f"maq: Saldo = {saldo_euros}e {saldo_centavos}c; Pedido = {preco_euros}e {preco_centavos}c")
    elif not (codigo in stock):
        print("maq: Produto não encontrado.")
    elif stock[codigo]["quantidade"] == 0:
        print("maq: Stock Insuficiente.")
    return stock, saldo

def token_parser(stock, saldo, t):
    if t.type == 'LISTAR': 
        listar_stock(stock)
    elif t.type == 'MOEDA':
        # Divide a string em palavras
        moedas = t.value[6:].split(',')
        
        # Verifica se há mais de uma palavra (ou seja, se há moedas após "MOEDA")
        if len(moedas) >= 1:
            # Itera sobre as moedas e as processa
            for moeda in moedas:
                if moeda.endswith('E'):
                    if (int(moeda[:-1]) <= 2):
                        saldo += int(moeda[:-1]) * 100
                    else: 
                        print(f"maq: Moeda Inválida: {moeda} .")
                elif moeda.endswith('C'): 
                    if (int(moeda[:-1]) == 1 or int(moeda[:-1]) == 2 or
                        int(moeda[:-1]) == 5 or int(moeda[:-1]) == 10 or
                        int(moeda[:-1]) == 20 or int(moeda[:-1]) == 50):
                        saldo += int(moeda[:-1])
                    else:
                        print(f"maq: Moeda Inválida: {moeda} .")
            print(f"maq: Saldo = {saldo // 100}e {saldo % 100}c .")
        else:
            print("maq: Nenhuma moeda fornecida.")
    elif t.type == 'SELECIONAR':
        code = t.value.split()[1]
        stock, saldo = comprar_produto(stock, saldo, code)
    elif t.type == 'ADD':
        add_produto(stock)
        print("maq: Stock atualizado: ")
        listar_stock(stock)
        save_stock(stock, "stock.json")
    elif t.type == 'REMOVE':
        code = t.value.split()[1]
        remover_produto(stock,code)
        print("maq: Stock atualizado: ")
        listar_stock(stock)
        save_stock(stock, "stock.json")
    elif t.type == 'UPDATE':
        listar_stock(stock)
        update(stock)
        print("maq: Produto atualizado: ")
        listar_stock(stock)
        save_stock(stock, "stock.json")
    elif t.type == 'HELP':
        help()
    return stock, saldo


def input_parser(stock, saldo):
    data_atual = datetime.now()
    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Olá! Estou disponível para atender o seu pedido.")
    
    while True:
        try:
            linha = input(">> ").strip().upper()
            if not linha:
                continue
            lexer.input(linha)
            while True:
                t = lexer.token()
                if not t:
                    break
                stock, saldo = token_parser(stock, saldo, t)
                if t.type == 'SAIR': # fazer o troco
                    print("maq: Até à próxima.")
                    return stock, saldo
        except KeyboardInterrupt:
            print("\nmaq: Operação interrompida. Até à próxima.")
            sys.exit(0)

def main():
    stock = load_stock("stock.json")
    saldo = 0
    stock, saldo = input_parser(stock, saldo)
    save_stock(stock, "stock.json")

if __name__ == "__main__":
    main()