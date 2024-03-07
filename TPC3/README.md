# TPC3: Somador on/off

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Este TPC consiste em desenvolver um programa que lê do stdin uma string e devolve como output a soma de todos os inteiros lidos na string enquanto o estado do programa for diferente de off (False).

Para este objetivo criei 2 variáveis auxiliares que me guardam o valor do inteiro lido até captar um caractere que não seja um digito (para representar números com mais de um digito) e o valor do estado on/off. Se forem lidos os caracteres "O", "N" e/ou "F" testo se a variável auxiliar criada é igual à string "on" ou "off" e realizo a mudança de estado adequada. 

Será imprimido um resultado por cada "=" que for encontrado na string de input.






























## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Para este TPC é necessário desenvolver um analisador léxico para uma linguagem de query como SQL.

Para este efeito, é necessário criar uma lista de tokens e associar expressões regulares (ou funções caso seja necessário definir comportamento adicional) a cada um, para podermos ler texto e capturar cada uma das palavras como um determinado token, para posterior tratamento de dados. 

Para este caso foram criados tokens para comandos, atributos (são um nao comando essencialmente), delimitadores, números e operadores. Claro que num *tokenizer* é importante definir os tokens para contagem de linhas, *error handling* e o token para ignorar "whitespaces". Em relação aos comandos, fez-se um tratamento muito geral (igual para todos os comandos) através do uso de um dicionário, evitando assim uma especificação diferente para todas as instruções existentes. Em especial atenção, este analisador é capaz de capturar comandos com mais do que uma palavra como o "group by".

Depois é necessário construir o lexer e passar-lhe input, que neste caso será o stdin. Depois de introduzida a linha que se pretende ler, o programa devolverá então a lista de tokens capturadas.