# Boas-vindas ao programa
import time
time.sleep(2)  # Adicionando uma pausa de 2 segundos para tornar a experiência mais interativa.
print("Bem vindo(a) à calculadora de IMC")

# Criando um loop principal para que o usuário possa calcular o IMC várias vezes
try:
    while True:
        # Recebendo os dados do usuário
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        # Calculando o IMC
        altura_calculada = altura ** 2  # A altura ao quadrado.
        calcular = peso / altura_calculada  # Fórmula do IMC.
        print("O seu IMC é: ", calcular)  # Exibindo o resultado.

        # Classificando o IMC com base no valor calculado
        if calcular <= 18.5:
            print("Seu IMC está classificado como magreza.")
        elif calcular <= 24.9:
            print("Seu IMC está classificado como normal.")
        elif calcular <= 29.9:
            print("Seu IMC está classificado como sobrepeso.")
        elif calcular <= 39.9:
            print("Seu IMC está classificado como obesidade.")
        else:
            print("Seu IMC está classificado como obeso")

        print("IMC menor que 18.5 (magreza)\n", "Entre 18,5 e 24,9 (normal)\n", "Entre 25,0 e 29,9 (sobrepeso)\n", "Entre 30,0 e 39,9 (obesidade)\n", "Maior que 40,0 (obesidade grave)\n")     

        # Opção para continuar ou sair do programa
        resposta = str(input("Deseja continuar? (s/n) \n"))
        if resposta != "s":  # Se o usuário não digitar "s", o loop será encerrado.
            break

    # Mensagem final ao usuário
    print("Fim.")
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para peso e altura.")

