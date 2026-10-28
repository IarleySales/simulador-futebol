import random

gols_casa = 0
gols_visitante = 0

lances = ["gol", "defesa", "falta", "escanteio", "pênalti"]
penalti = ["gol", "gol", "gol" "gol", "gol", "gol", "defesa", "defesa", "erro", "erro"]

time_casa = input("Escolha o time da casa: ").upper()
time_visitante = input("Escolha o time visitante: ").upper()
estadio = input(f"Escolha o estádio para a partida entre {time_casa} e {time_visitante}: ").upper()

print(f"========{time_casa} x {time_visitante}========")
print(f"A BOLA ROLA NO {estadio}\n")

for minuto in range(1, 93):
    sorteio = random.randint(1, 1000)

    if sorteio <= 50:
        time_gol = random.choice([time_casa, time_visitante])
        print(f"{minuto}' - GOL do {time_gol}!")

        if time_gol == time_casa:
            gols_casa += 1
        else:
            gols_visitante += 1

        print(f"{time_casa} {gols_casa} x "
              f"{gols_visitante} {time_visitante}\n")

    elif sorteio <= 100:
        print(f"{minuto}' - Boa chance de gol! Mas o goleiro faz a defesa.")

    elif sorteio <= 150:
        print(f"{minuto}' - Falta cometida! O juiz marca a falta para o(a) {random.choice([time_casa, time_visitante])}")

    elif sorteio <= 200:
        print(f"{minuto}' - Escanteio para o(a) {time_casa}")

    elif sorteio == 207:
        print(f"{minuto}' - Pênalti para o(a) {time_visitante}")

        resultado_penalti = random.choice(penalti)

        if resultado_penalti == "gol":
            gols_visitante += 1
            print(f"{minuto}' - GOL DO(a) {time_visitante} DE PENALTIII!")

        elif resultado_penalti == "defesa":
            print(f"{minuto}' - O GOLEIRO DO(a) {time_casa} DEFEEENDEEE O PÊNALTI!")

        else:
            print(f"{minuto}' - O JOGADOR DO {time_visitante} DESPERDIÇA O PÊNALTI!")

        print(f"Placar: {time_casa} {gols_casa} x "f"{gols_visitante} {time_visitante}\n")
print(f"========TERMINA A PARTIDA!========")
print(f"{time_casa} {gols_casa} x {gols_visitante} {time_visitante}")

if gols_casa > gols_visitante:
    print(f"{time_casa} VENCE A PARTIDA")
elif gols_casa < gols_visitante:
    print(f"{time_visitante} VENCE A PARTIDA")
else:
    print("A PARTIDA TERMINA EMPATADA")
