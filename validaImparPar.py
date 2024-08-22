# Atribuindo o valor a variável
valorVariavel = 1

# Começar a percorrer o array
while valorVariavel < 11:

    # Fazendo a validação se o número é impar ou par
    if (valorVariavel % 2) == 0:

        # Colando as informações na variavel para imprimir na tela
        resultadoValorVariavel = f" O valor é {valorVariavel} é par" 

    else:

        # Colando as informações na variavel para imprimir na tela
        resultadoValorVariavel = f" O valor é {valorVariavel} é impar" 

    # Imprimindo na tela o resultado
    print(resultadoValorVariavel)

    # Atualizando o valor da variável para evitar loop infinito
    valorVariavel += 1
