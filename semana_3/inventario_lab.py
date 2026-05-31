import sys

# Base de dados dos reagentes

reagentes = [
    'Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno',
    'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno',
    'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno',
    'Ácido Sulfúrico', 'Metanol', 'Ácido Acético', 'Etanol',
    'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol',
    'Acetona', 'Metanol', 'Ácido Sulfúrico', 'Acetona',
    'Ácido Acético', 'Etanol'
]

lotes = [
    '2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
    '2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01',
    '2023-MET-01', '2024-TOL-01', '2023-ETA-01', '2023-ACE-01',
    '2023-ACA-01', '2023-ETA-02', '2023-BEN-01', '2023-SUL-01',
    '2023-MET-01', '2024-ACA-01', '2023-ETA-01', '2023-ACE-01',
    '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
    '2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01',
    '2024-ACA-01', '2023-ETA-02'
]

purezas = [
    99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0,
    98.8, 99.5, 92.0, 99.2, 96.0, 99.9, 98.0, 99.0, 95.0,
    99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0,
    98.5, 95.0, 96.0
]

# Analisando o inventário

reagentes_unicos = set(reagentes)

print("=== REAGENTES DISPONIVEIS ===")
print(reagentes_unicos)
print(f"Quantidade de reagentes diferentes: {len(reagentes_unicos)}")

inventario = list(zip(reagentes, lotes, purezas))

# Exibindo o inventário completo

print("\n=== RELATORIO DO INVENTARIO ===")

for reagente, lote, pureza in inventario:
    print(
        f"Frasco do Lote: {lote} | "
        f"Reagente: {reagente} | "
        f"Pureza: {pureza}%"
    )

# List comprehension
lotes_aprovados = [
    lote
    for reagente, lote, pureza in inventario
    if pureza >= 98.0
]

print("\n=== LOTES APROVADOS ===")
print(lotes_aprovados)