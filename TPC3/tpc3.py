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
