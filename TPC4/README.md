# TPC3: Analisador Léxico para linguagem SQL

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Para este TPC é necessário desenvolver um analisador léxico para uma linguagem de query como SQL.

Para este efeito, é necessário criar uma lista de tokens e associar expressões regulares (ou funções caso seja necessário definir comportamento adicional) a cada um, para podermos ler texto e capturar cada uma das palavras como um determinado token, para posterior tratamento de dados. 

Para este caso foram criados tokens para comandos, atributos (são um nao comando essencialmente), delimitadores, números e operadores. Claro que num *tokenizer* é importante definir os tokens para contagem de linhas, *error handling* e o token para ignorar "whitespaces". Em relação aos comandos, fez-se um tratamento muito geral (igual para todos os comandos) através do uso de um dicionário, evitando assim uma especificação diferente para todas as instruções existentes. Em especial atenção, este analisador é capaz de capturar comandos com mais do que uma palavra como o "group by".

Depois é necessário construir o lexer e passar-lhe input, que neste caso será o stdin. Depois de introduzida a linha que se pretende ler, o programa devolverá então a lista de tokens capturadas.