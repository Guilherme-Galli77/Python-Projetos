while True:

    print("======================================================================================")
    print("                           CALCULADORA DA EQUAÇÃO DE DRAKE                            ")
    print("======================================================================================")
    print("OBS: Digitar as fraçoes como valores com casas decimais, exemplo 0.44, 0.67 , etc....")
    print("======================================================================================")

    r = int(input("Digite a taxa de formação de estrelas em nossa galáxia (considerando o periodo de 1 ano): "))
    fp = float(input("Digite a fração de estrelas com sistemas planetários: (estudos estimam 0,5) "))
    ne = int(input("Digite o número de planetas, por sistema estelar, com um ambiente adequado para a vida: "))
    fl = float(input("Digite a fração de planetas adequados em que a vida realmente possa se desenvolver: "))
    fi = float(input("Digite a fração de planetas que desenvolvem vida inteligente: "))
    fc = float(input("A fração de planetas com vida inteligente e que têm o desejo e os meios necessários para "
                     "estabelecer comunicação: "))
    l = int(input("Digite o tempo esperado de vida de tal civilização: (estudos indicam 10000 anos) "))

    n = r*fp*ne*fl*fi*fc*l
    print("======================================================================================")
    print(f"O número de civilizações na Via Láctea com as quais poderíamos estabelecer contato é {n} !!!! ")
    print("======================================================================================")
    cont = ""
    while cont != "N" and cont != "S":
        cont = str(input("Deseja calcular novos valores? [S/N] ")).strip().upper()
    if cont == "N":
        break
print("======================================================================================")
print("Obrigado por usar a calculadora")
