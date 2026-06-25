# LÓGICA FUZZY: MODELO TAKAGI-SUGENO (ORDEM ZERO)
# Sistema de Frenagem Inteligente do Metrô

# 1. FUNÇÃO DE PERTINÊNCIA (Fuzzificação)
# Uma função matemática super simples para criar os "triângulos" da Lógica Fuzzy
def grau_triangulo(x, inicio, pico, fim):
    if x <= inicio or x >= fim: return 0.0      # Fora do triângulo
    if x == pico: return 1.0                    # No topo do triângulo
    if x < pico: return (x - inicio) / (pico - inicio) # Subida
    if x > pico: return (fim - x) / (fim - pico)       # Descida

# --- INÍCIO DO PROGRAMA ---

# Leitura dos Sensores (Entradas exatas)
velocidade = 80  # km/h
distancia = 200  # metros

print(f"Sensores -> Velocidade: {velocidade} km/h | Distância: {distancia} m")

# 2. FUZZIFICAÇÃO (Calculando os "graus" de verdade de 0 a 1)
# Verificando as categorias de velocidade
vel_media = grau_triangulo(velocidade, 20, 50, 90)
vel_alta = grau_triangulo(velocidade, 60, 100, 150)

# Verificando as categorias de distância
dist_perto = grau_triangulo(distancia, -100, 0, 300)
dist_media = grau_triangulo(distancia, 150, 500, 800)

# 3. BASE DE REGRAS DE SUGENO (O Cérebro)
# Diferente do Mamdani, a saída aqui é um NÚMERO EXATO (Constante), não um conceito.

# Regra 1: SE Velocidade Alta E Distância Perto -> FREIO = 90%
# O operador "E" na lógica fuzzy é o valor mínimo entre as duas variáveis
peso_r1 = min(vel_alta, dist_perto)
saida_r1 = 90  

# Regra 2: SE Velocidade Média E Distância Média -> FREIO = 50%
peso_r2 = min(vel_media, dist_media)
saida_r2 = 50  

# 4. DEFUZZIFICAÇÃO (A Mágica da Eficiência)
# Em vez de calcular áreas e centro de gravidade (geometria pesada),
# Sugeno faz apenas uma MÉDIA PONDERADA simples!

soma_dos_pesos = peso_r1 + peso_r2

if soma_dos_pesos > 0:
    # Fórmula: (Peso1 * Saida1 + Peso2 * Saida2) / Total_de_Pesos
    freio_final = (peso_r1 * saida_r1 + peso_r2 * saida_r2) / soma_dos_pesos
else:
    freio_final = 0.0

print(f"\nDECISÃO DA IA: Força aplicada no freio será de {freio_final:.2f}%")
