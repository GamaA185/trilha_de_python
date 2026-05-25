import sys
def titulo():
    print("="*50)
    print("      CALCULADORA DE ORÇAMENTO DE VIAGENS      ")
    print("="*50)

def calculo_e_resultados():
    try:
        orcamento_disponivel_reais = float(input("Qual o seu orçamento disponível em reais? "))
        custo_da_passagem_reais = float(input("Qual o custo da passagem em reais? "))
        custo_diario_hospedagem_euros = float(input("Qual o custo diário da hospedagem em euros? "))
        qtde_de_dias = int(input("Quantos dias de viagem? "))
        destino = input("Qual o seu destino? ").strip()
        if not destino or not all(c.isalpha() or c == " " for c in destino):
            print("Erro: o destino deve conter apenas letras e espaços.")
            sys.exit()

        if (
            orcamento_disponivel_reais < 0
            or custo_da_passagem_reais < 0
            or custo_diario_hospedagem_euros < 0
            or qtde_de_dias < 0
        ):
            print("Erro: nenhum valor numérico pode ser negativo.")
            sys.exit()
        else:
            cotacao_euro = 6.10

            custo_diario_hospedagem_reais = custo_diario_hospedagem_euros * cotacao_euro
            valor_total_hospedagem_reais = custo_diario_hospedagem_reais * qtde_de_dias
            custo_total_reais = custo_da_passagem_reais + valor_total_hospedagem_reais

            orcamento_possivel = custo_total_reais <= orcamento_disponivel_reais
            viagem_viavel = orcamento_possivel and qtde_de_dias > 0

            diferenca = orcamento_disponivel_reais - custo_total_reais

            print("\nResumo da viagem")
            print(f"Destino: {destino}")
            print(f"Orçamento disponível: R$ {orcamento_disponivel_reais:.2f}")
            print(f"Valor total da hospedagem: R$ {valor_total_hospedagem_reais:.2f}")
            print(f"Custo total da viagem: R$ {custo_total_reais:.2f}")

            if orcamento_possivel:
                print("Status do orçamento: Orçamento possível")
            else:
                print("Status do orçamento: Orçamento não possível")

            if viagem_viavel:
                print("Status final: Viável")
            else:
                print("Status final: Inviável")

            if diferenca >= 0:
                print(f"Sobra: R$ {diferenca:.2f}")
            else:
                print(f"Falta: R$ {abs(diferenca):.2f}")

    except ValueError:
        print("Erro: Por favor, insira um valor válido.")
        sys.exit()
titulo()
calculo_e_resultados()
