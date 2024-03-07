# TPC3: Somador on/off

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Este TPC consiste em desenvolver um programa que lê do stdin uma string e devolve como output a soma de todos os inteiros lidos na string enquanto o estado do programa for diferente de off (False).

Para este objetivo criei 2 variáveis auxiliares que me guardam o valor do inteiro lido até captar um caractere que não seja um digito (para representar números com mais de um digito) e o valor do estado on/off. Se forem lidos os caracteres "O", "N" e/ou "F" testo se a variável auxiliar criada é igual à string "on" ou "off" e realizo a mudança de estado adequada. 

Será imprimido um resultado por cada "=" que for encontrado na string de input.
