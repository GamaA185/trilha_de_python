import sys

def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    hp_defensor -= ataque

    if hp_defensor < 0:
        hp_defensor = 0
    print(f"{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!")
    print(f"{nome_defensor} agora possui {hp_defensor} HP.")

    return hp_defensor


def exibir_placar(nome1, hp1, nome2, hp2):
    print("\n===== PLACAR =====")
    print(f"{nome1}: {hp1} HP")
    print(f"{nome2}: {hp2} HP")
    print("==================")


# Entradas
nome_monstro1 = input("Nome do Monstro 1: ").strip()
nome_monstro2 = input("Nome do Monstro 2: ").strip()

# Validação de nomes
if nome_monstro1 == "" or nome_monstro2 == "":
    print("Erro: os monstros precisam possuir nomes válidos!")
    sys.exit()

try:
    hp_monstro1 = int(input("HP do Monstro 1: "))
    ataque_monstro1 = int(input("Ataque do Monstro 1: "))

    hp_monstro2 = int(input("HP do Monstro 2: "))
    ataque_monstro2 = int(input("Ataque do Monstro 2: "))

except ValueError:
    print("Erro: digite apenas números inteiros!")
    sys.exit()

# Validação de valores
if (
    hp_monstro1 <= 0 or
    ataque_monstro1 <= 0 or
    hp_monstro2 <= 0 or
    ataque_monstro2 <= 0
):
    print("Erro: HP e ataque devem ser maiores que zero!")
    sys.exit()


turno = 1

while hp_monstro1 > 0 and hp_monstro2 > 0:

    print(f"\n========== TURNO {turno} ==========")

    # Monstro 1 ataca
    hp_monstro2 = atacar(
        nome_monstro1,
        ataque_monstro1,
        nome_monstro2,
        hp_monstro2
    )

    # Monstro 2 revida apenas se sobreviver
    if hp_monstro2 > 0:
        hp_monstro1 = atacar(
            nome_monstro2,
            ataque_monstro2,
            nome_monstro1,
            hp_monstro1
        )

    exibir_placar(
        nome_monstro1,
        hp_monstro1,
        nome_monstro2,
        hp_monstro2
    )

    turno += 1


print("\n===== FIM DA BATALHA =====")

# Validação sobre quem venceu usando estrutura condicional
if hp_monstro1 > 0:
    print(f"{nome_monstro1} venceu o duelo!")
else:
    print(f"{nome_monstro2} venceu o duelo!")
