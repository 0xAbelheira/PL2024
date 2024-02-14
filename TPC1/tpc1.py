import matplotlib.pyplot as plt
import numpy as np

def read_file(path):
    try:
        file = open(path, "r") # abrir em modo de leitura
        f = file.readlines()
        f.pop(0) # eliminar header (só se pode fazer pop depois de ler o ficheiro)
        file.close()
        return f

    except FileNotFoundError:
        print(f"{path} file not found!")
        exit(1)
    
def sort_lists(lst):
    l = (set(lst)) # eliminar elementos repetidos
    return sorted(l)

def distrib_age(age_list, extremes):
    max = extremes["age"]["max"]
    min = extremes["age"]["min"]
    distrib = {}

    for i in range(0, max // 5 + 1):
        distrib[(i*5,i*5 + 4)] = { "count" : 0 }

    for age in age_list:
        intervalo = age // 5
        distrib[(intervalo*5, intervalo*5 + 4)]["count"] += 1

    return distrib

def tabela_distribuicao(distribuicao):
    # Define a tabela como uma lista de listas
    tabela = [["Intervalos", "Frequência"]]
    
    for key in distribuicao.keys():
        tabela += [[str(key), str(distribuicao[key]["count"])]]

    # Define o número de colunas e linhas da tabela
    num_colunas = len(tabela[0])
    num_linhas = len(tabela)

    # Define a largura das colunas
    larguras = [max(len(tabela[i][j]) for i in range(num_linhas)) for j in range(num_colunas)]

    # Imprime a tabela
    for i in range(num_linhas):
        for j in range(num_colunas):
            print("{:{}}".format(tabela[i][j], larguras[j]), end="  ")
        print()

def distribuicaoGrafico(distribuicao):
    x_eixo = np.arange(len(distribuicao.keys()))
    x_coords = [str(elem) for elem in distribuicao.keys()]
    y_cd = [elem["count"] for elem in distribuicao.values()]

    plt.figure(figsize=[12, 7])

    plt.barh(x_eixo - 0.2, y_cd, color = "skyblue", label="Frequência", tick_label=x_coords, height=0.4)

    plt.yticks(x_eixo, distribuicao.keys())
    plt.xlabel("Frequência Absoluta")
    
    plt.title("Distribuição por Escalão Etário")

    plt.legend()
    plt.show()


def main():
    mods = []
    total_athl = 0
    capable_athl = 0
    extremes = { "age": {"max": 0, "min": 0} }
    age_list = []


    f = read_file("emd.csv")

    for line in f:
        line = line.replace("\n","")
        lines = line.split(",")

        mods.append(lines[8])
        
        total_athl += 1
        if (lines[12].lower() == "true"):
            capable_athl += 1
        
        age = int(lines[5])
        age_list.append(age)

        if age > extremes["age"]["max"]:
            extremes["age"]["max"] = age
        elif age < extremes["age"]["min"]:
            extremes["age"]["min"] = age

    mods_ord = sort_lists(mods)
    print()
    print("Lista ordenada alfabeticamente das modalidades:")
    print(mods_ord)
    print() # já inclui o \n

    capable_athl_P = (capable_athl / total_athl) * 100
    uncapable_athl_P = 100 - capable_athl_P

    print(f"Percentagem de atletas aptos para a prática desportiva: {capable_athl_P}%")
    print(f"Percentagem de atletas inaptos para a prática desportiva: {uncapable_athl_P}%")
    print() 
    
    print("Tabela de Distribuição:")
    distr = distrib_age(age_list, extremes)
    tabela_distribuicao(distr)
    print()
    
    print("Gráfico da Distribuição:")
    print("Uma janela com o gráfico foi gerada com sucesso!")
    distribuicaoGrafico(distr)

if __name__ == "__main__":
    main()

