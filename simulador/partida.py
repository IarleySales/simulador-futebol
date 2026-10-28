import random
import time

gols_casa = 0
gols_visitante = 0

lances = ["gol", "defesa", "falta", "escanteio", "pênalti"]
penalti = ["gol", "gol", "gol", "gol", "gol", "gol", "defesa", "defesa", "erro", "erro"]

time_casa = input("Escolha o time da casa: ").upper()
time_visitante = input("Escolha o time visitante: ").upper()
estadio = input(f"Escolha o estádio para a partida entre {time_casa} e {time_visitante}: ").upper()

print(f"======== {time_casa} x {time_visitante} ========")
print(f"A BOLA ROLA NO {estadio}\n")

for minuto in range(1, 93):
    time.sleep(0.3)
    sorteio = random.randint(1, 1000)

    if sorteio <= 50:
        time_gol = random.choice([time_casa, time_visitante])
        print(f"{minuto}' - GOL do {time_gol}!")

        if time_gol == time_casa:
            gols_casa += 1
        else:
            gols_visitante += 1

        print(f"{time_casa} {gols_casa} x {gols_visitante} {time_visitante}\n")

    elif sorteio <= 100:
        print(f"{minuto}' - GRANDE CHANCE DE GOL! MAS O GOLEIRÃO FAZ A DEFESA")

    elif sorteio <= 170:
        time_falta = random.choice([time_casa, time_visitante])
        print(f"{minuto}' - Falta cometida! O juiz marca a falta para o(a) {time_falta}")

    elif sorteio <= 210:
        time_escanteio = random.choice([time_casa, time_visitante])
        print(f"{minuto}' - Escanteio para o(a) {time_escanteio}")

    elif sorteio <= 215:
        time_penalti = random.choice([time_casa, time_visitante])
        print(f"{minuto}' - Pênalti para o(a) {time_penalti}")

        resultado_penalti = random.choice(penalti)

        if resultado_penalti == "gol":
            if time_penalti == time_casa:
                gols_casa += 1
            else:
                gols_visitante += 1

            print(f"{minuto}' - GOL DO(A) {time_penalti} DE PENALTIII!")

        elif resultado_penalti == "defesa":
            if time_penalti == time_casa:
                time_goleiro = time_visitante
            else:
                time_goleiro = time_casa

            print(f"{minuto}' - O GOLEIRO DO(A) {time_goleiro} DEFENDE O PÊNALTI!")

        else:
            print(f"{minuto}' - O JOGADOR DO(A) {time_penalti} DESPERDIÇA O PÊNALTI!")

        print(f"Placar: {time_casa} {gols_casa} x {gols_visitante} {time_visitante}\n")

    if minuto == 45:
        print("\n======== INTERVALO ========\n")
        time.sleep(5)
        print("COMEÇA O SEGUNDO TEMPO\n")

print("\n======== TERMINA A PARTIDA! ========")
print(f"{time_casa} {gols_casa} x {gols_visitante} {time_visitante}")

if gols_casa > gols_visitante:
    print(f"{time_casa} VENCE A PARTIDA")
elif gols_casa < gols_visitante:
    print(f"{time_visitante} VENCE A PARTIDA")
else:
    print("A PARTIDA TERMINA EMPATADA")
