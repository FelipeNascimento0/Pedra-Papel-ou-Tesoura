from random import*

opc = ["pedra","papel","tesoura"]

continuar = "s"
vitorias = 0 
derrotas = 0
empate = 0  

while continuar == "s":
    print("vamos começar")
    escolha = input("Pedra, Papel ou Tesoura? ")
    esc_pc = choice(opc)
    if not escolha == opc :
        print('[ERRO]Não existe essa opção! escolha entre: pedra, papel ou tesoura. ')
        break
    if esc_pc == "pedra":
        print("Computador escolheu: " + str.capitalize(esc_pc))
        if escolha == "pedra":
            print("EMPATE")
            empate += 1
        elif escolha == "papel":
            print("VITORIA!")
            vitorias += 1
        elif escolha == "tesoura":
            print("DERROTA")
            derrotas += 1
        else:
            print("Algo de errado não está certo")

    if esc_pc == "papel":
        print("Computador escolheu: " + str.capitalize(esc_pc))
        if escolha == "pedra":
            print("DERROTA")
            derrotas += 1
        elif escolha == "papel":
            print("EMPATE!")
            empate += 1
        elif escolha == "tesoura":
            print("VITORIA!")
            vitorias += 1
        else:
            print("Algo de errado não está certo")

    if esc_pc == "tesoura":
        print("Computador escolheu: " + str.capitalize(esc_pc))
        if escolha == "pedra":
            print("VITORIA")
            vitorias += 1
        elif escolha == "papel":
            print("DERROTA!")
            derrotas += 1
        elif escolha == "tesoura":
            print("EMPATE")
            empate += 1
        else:
            print("Algo de errado não está certo")
    print("RESULTADOS")
    print("\nVITORIAS " + str(vitorias))
    print("\nEMPATES " + str(empate))
    print("\nDERROTAS " + str(derrotas))

    if not (input("Quer continuar?[s/n] ") == "s"):
        break 