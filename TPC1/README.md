# TPC1: Análise de um Dataset

## Autor
Hugo Abelheira (A95151)

## Desenvolvimento
Neste trabalho fiz a leitura e processamento dos dados contidos num ficheiro csv fornecido pelos docentes.

O objetivo aqui é mostrar algumas métricas como a lista ordenada alfabeticamente das modalidades, as percentagens de atletas aptos e inaptos a praticar desporto bem como a distribuição dos atletas por faixa etária.

Comecei por desenvolver um parser bastante simples para realizar a leitura do csv e dividir a informação por linhas. Depois fiz uma função que ordena listas, transformando-as primeiro em conjuntos para eliminar elementos repetidos. Depois para a distribuição por faixa etária, o verdadeiro desafio do problema em questão, criei uma lista que contém todas as idades bem como um dicionário para guardar a idade mínima e máxima. Através destas estruturas e da informação com que as preenchi, criei um novo dicionário com a distribuição pretendida.
No final, criei uma tabela de distribuição e um gráfico para ter alternativas de visualização do resultado pretendido.
