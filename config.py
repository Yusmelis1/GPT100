# ==========================
# GPT-100 PRO CONFIGURATION
# ==========================

# PESOS DEL MÉTODO GPT-100

FORM_WEIGHT = 25
ATTACK_WEIGHT = 20
DEFENSE_WEIGHT = 25
OPPONENT_WEIGHT = 20
OTHER_WEIGHT = 10

TOTAL_SCORE = 100


# CLASIFICACIÓN GPT-100

LEVEL_S = 15      # Diferencia >= 15 puntos
LEVEL_A = 9       # Diferencia 9-14
LEVEL_B = 5       # Diferencia 5-8
LEVEL_C = 0       # Menor de 5


# CONFIANZA

CONFIDENCE_S = "⭐⭐⭐⭐⭐"
CONFIDENCE_A = "⭐⭐⭐⭐☆"
CONFIDENCE_B = "⭐⭐⭐☆☆"
CONFIDENCE_C = "No apostar"


# MERCADOS RECOMENDADOS

SAFE_MARKETS = [
    "1X2",
    "DNB",
    "Doble oportunidad",
    "Más de 1.5 goles"
]
