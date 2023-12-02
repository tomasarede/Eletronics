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
    (convert_to_rad([100, 1000, 2500, 3000, 3500, 4000, 4200, 5000, 6000, 10000, 20000, 100000]),
     convert_to_db([0.13, 1.15, 3.18, 3.9, 4.3, 4.5, 4.4, 4, 3.18, 1.79, 0.86, 0.17]),
     [0, -42570.22, 0],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 4998 OHM',
     '|T1(s)|',
     'Pontos Experimentais',
     'blue'
     ),
    (convert_to_rad([2000, 2500, 3000, 3500, 4000, 4500, 4750, 5000]),
     convert_to_db([5, 5.1, 5.1, 4.8, 4.3, 3.62, 3.3, 3.02]),
     [0, 0, -905749352.706],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 4998 OHM',
     '|T2(s)|',
     'Pontos Experimentais',
     'red'
     ),
    (convert_to_rad([2500, 2700, 4600]),
     convert_to_db([5.1, 5.2, 3.58]),
     [0, 0, 905749352.706],
     [1, 2.128e4, 4.527e8],
     'T1(s), T2(s) e T3(s) em comparação com os pontos experimentais - P2 = 4998 OHM',
     '|T3(s)|',
     'Pontos Experimentais',
     'green'
     )
]

# Configurar o gráfico
plt.figure(figsize=(10, 6))
for w, db, num, den, title, label1, label2, color in data_sets:
    plot(w, db, num, den, 1000, 1000000, -40, 20, title, label1, label2, color)

plt.show()
