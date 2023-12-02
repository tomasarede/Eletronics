









import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction
from scipy.signal import bode

def convert_to_rad(frequencias):
    return [2 * np.pi * f for f in frequencias]

def convert_to_db(voltagens):
    return [20 * np.log10(V/2) for V in voltagens]

def plot(w, db, numerator, denominator, xinf, xsup, yinf, ysup, title, label1, label2, color):
    sys = TransferFunction(numerator, denominator)
    w_response, mag_response, _ = bode(sys)
    
    w_high = np.logspace(0, 6, num=1000)
    _, mag_response_high, _ = bode(sys, w_high)

    plt.semilogx(w_high, mag_response_high, label=label1, color=color, lw=2)  # Curvas teóricas escuras
    plt.plot(w, db, linestyle=' ', marker='o', label=label2, color=color, alpha=0.5)  # Pontos experimentais mais claros

    plt.xlabel('Frequência (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.title(title)
    plt.grid(True)
    plt.legend()

    plt.xlim(xinf, xsup)
    plt.ylim(yinf, ysup)

# Coletar todos os dados em uma lista
data_sets = [
    (convert_to_rad([2300,3800,6100]),
     convert_to_db([13.1/0.5,18.7/0.5,13.2/0.5]),
     [0, -421151.934772, 0],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 505.2 OHM',
     '|T1(s)|',
     'Pontos Experimentais',
     'blue'
     ),
    (convert_to_rad([2900,4540]),
     convert_to_db([21.7/0.5,15.3/0.5]),
     [0,0, 8.9606794632e9],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 505.2 OHM',
     '|T2(s)|',
     'Pontos Experimentais',
     'red'
     ),
    (convert_to_rad([3000,4500]),
     convert_to_db([18.1/0.4,12.9/0.4]),
     [0,0, -8.9606794632e9],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 505.2 OHM',
     '|T3(s)|',
     'Pontos Experimentais',
     'green'
     )
]

# Configurar o gráfico
plt.figure(figsize=(10, 6))
for w, db, num, den, title, label1, label2, color in data_sets:
    plot(w, db, num, den, 1000, 1000000, -40, 40, title, label1, label2, color)

plt.show()





