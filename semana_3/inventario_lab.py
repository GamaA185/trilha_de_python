import sys

reagentes_unicos = set(reagentes)

print("=== REAGENTES DISPONIVEIS ===")
print(reagentes_unicos)
print(f"Quantidade de reagentes diferentes: {len(reagentes_unicos)}")

inventario = list(zip(reagentes, lotes, purezas))


print("\n=== RELATORIO DO INVENTARIO ===")

for reagente, lote, pureza in inventario:
    print(
        f"Frasco do Lote: {lote} | "
        f"Reagente: {reagente} | "
        f"Pureza: {pureza}%"
    )