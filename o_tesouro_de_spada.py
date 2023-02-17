# O desafio era criar um jogo, dando alternativas e, dependendo da escolha, teria uma consequência, positiva ou negativa.
# Eu aproveitei a oportunidade para refletir sobre isso... todas as escolhas que fazemos trazem consequências...
# a minha escolha pela tecnologia não foi muito óbvia para mim, mas descobri um tesouro nessa área... Eu me reencontrei!
# Essa é a dica que eu deixo: nem sempre o caminho mais óbvio é que o vai te guiar para um lugar melhor. Persista e tenha foco!



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo(a) à Ilha de Monte Cristo.\nSua missão é encontrar o Tesouro de Spada.\n")

again = "sim"

while again == "sim":
    left_right = input("Você entra numa gruta e agora está está em uma encruzilhada. Onde você quer ir? Digite 'esquerda' ou 'direita'\n")
    if left_right == 'esquerda':
        print("Você escuta a voz de conde Mondego, que te seguiu até certa parte e também está dentro da gruta.")
        back_continue = input("O que você quer fazer? Digite 'retornar' ou 'continuar'.\n")
        if back_continue == "retornar":
            print("Você chega a um lago de lindas águas azul turqueza.")
            jump_walk = input("Você pula na água ou continua andando pela gruta? Digite 'pular' ou 'andar'.\n")
            if jump_walk == "andar":
                print("Você continua andando, e vê um outro lago com água não tão cristalinas e neste, há algumas rochas ponteagudas.")
                final = input("Você entra na água, volta para o outro lago ou continua andando pela gruta? Digite 'entrar', 'voltar' ou 'andar'.\n")
                if final == "entrar":
                    print("*** Você encontra o tesouro! Você retira as arcas do fundo do lago e as coloca dentro do barco!")
                    print("Você se junta a Mercédès, o Albert, Jacopo e começa uma nova jornada!")
                    print("Boa sorte! ***")
                elif final == "go back":
                    print("Ah não, o lago é mais raso do que parece... você se machuca em uma rocha. GAME OVER!")
                else:
                    print("Você dá de cara com o Conde Mondego e é mandado para o Chatêau d'If de novo... GAME OVER!")
            else:
                print("Ah não, o lago é mais raso do que parece... você se machuca em uma rocha. GAME OVER!")
        else:
            print("Você é capturado pelo conde Mondego e mandado de volta para o Chatêau d'If...\nGAME OVER!")
    else:
        print("Ah não! Há um buraco logo na curva. Você caiu lá.\nGAME OVER!")

    again = input("\nVamos jogar de novo? Digite 'sim' ou 'nao': ")

print("Fim")

