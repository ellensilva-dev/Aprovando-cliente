# Avaliação para Aluguel

Programa em Python que simula a análise de aprovação de um aluguel na "Central de Aluguel da Cars". Ele pergunta alguns dados ao usuário e verifica, uma por uma, as exigências para ser aprovado.

## Exigências verificadas

1. Possuir fiador
2. Ter renda mensal de pelo menos 3 vezes o valor do aluguel
3. Possuir seguro

## Como usar

1. Tenha o Python 3 instalado.
2. Execute no terminal:

   ```bash
   python avaliacao_aluguel.py
   ```

3. Responda às perguntas do programa: nome, renda mensal, valor do aluguel, se possui fiador e se possui seguro (responda `sim` ou `não`).

## Exemplo de execução

```
Para iniciarmos, digite seu nome: Maria
Sr(a) Maria, qual é o valor da sua renda mensal atualmente? R$3000
Qual é o valor do aluguel? R$1000
O(a) Sr(a) possui fiador? sim
E seguro, o(a) Sr(a) possui seguro? sim
----------PROCESSANDO----------
Primeiro passo está dentro de nossas exigencias, o(a) Sr(a) possui fiador!
Calculando a sua renda, que está no valor de: R$3000 e o aluguel R$1000, a renda está aprovado(a)!
Nossa 3° exigência está cumprida, o(a) Sr(a) possui seguro!
```

## O que pratiquei

- Entrada de dados com `input()` e conversão de tipos com `int()`
- Estruturas condicionais (`if` / `else`)
- Operações matemáticas e comparações
- Formatação de textos com f-strings

## Próximos passos

- Mostrar uma mensagem final de "aprovado" ou "reprovado" quando as três exigências forem cumpridas
- Aceitar valores decimais na renda e no aluguel
- Aceitar respostas como "Sim" e "SIM", e não só "sim"
