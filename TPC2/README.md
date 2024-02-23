# TPC2: Conversor de MD para HTML

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Este trabalho consistiu em desenvolver um pequeno conversor de MD para HTML limitado a uma sintaxe bastante básica. 

Desenvolvi expressões regulares para cada elemento html que pretendia implementar no conversor, nomeadamente, cabeçalhos, negritos, itálicos, listas numeradas, links e imagens. 

Alguns casos extremos foram tidos em conta como a sobreposição de negritos e itálicos ao mesmo texto, listas no final do ficheiro e links dentro de links. Para além disso também usei as expressões regulares para não converter alguns possíveis erros de sintaxe, como whitespaces antes ou depois de negritos.

O conversor em si trata-se de uma série de condições onde vou tentar dar match linha a linha do respetivo elemento consoante a expressão regular adequada, substituindo a sintaxe de MD pela correspondente em HTML.

O ficheiro de input tem que ser passado como argumento ao programa, já sendo fornecido um exemplo. Para compilação do sistema temos então:

- python3 conversor.py input.md

O programa main() cria o ficheiro de output HTML e trata ainda de uma funcionalidade das listas numeradas.
