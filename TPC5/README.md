# TPC5: Máquina de Venda Automática

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Este projeto consiste na criação de uma Máquina de Venda Automática (MVA) capaz de gerenciar um stock de produtos e lidar com transações monetárias.

A MVA foi desenvolvida utilizando Python e Ply, uma ferramenta para construção de analisadores léxicos e sintáticos em Python. Esta ferramenta foi útil para a criação de tokens que vão corresponder aos comandos que a máquina deverá executar.

A máquina está sempre à espera de input e quando captura um token que corresponde a um dos comandos, executará a respetiva função. 

A base de dados (o stock) é mantida num ficheiro json e atualizada em runtime durante a execução da máquina, não permitindo a venda de produtos cujo stock já tenha terminado e assegurando que alterações (como novos produtos ou remoção de outros) no stock sejam também tidos em conta durante a interação com o utilizador.

### Funcionalidades
Listar Stock (LISTAR): Visualizar os produtos disponíveis na máquina, incluindo código, nome, quantidade e preço de cada produto.

Inserir Moeda (MOEDA): Os usuários podem inserir moedas na máquina, atualizando seu saldo. A máquina aceita apenas moedas válidas.

Selecionar Produto (SELECIONAR): Permite selecionar um produto para compra. Se o saldo for suficiente e houver stock disponível, o produto é dispensado e o saldo é atualizado.

Adicionar Produto (ADD): Adicionar um novo produto ao stock da máquina.

Remover Produto (REMOVE): Remover um produto do stock da máquina.

Atualizar Produto (UPDATE): Atualizar informações de um produto existente no estoque.

Ajuda (HELP): Permite visualizar todos os comandos disponíveis.

### Utilização
Para executar a MVA, basta correr a script Python tpc5.py. O utilizador deve começar pelo comando help, para ter acesso aos comandos existentes bem como os seus argumentos.

O programa termina quando o token "SAIR" for capturado ou o utilizador interromper o programa (CTRL+C).
