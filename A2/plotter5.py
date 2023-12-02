import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction
from scipy.signal import bode



def plot(x, y, z, w,k, xinf, xsup, yinf, ysup, title, label1, label2, label3, label4):
    # Calcular os valores da magnitude da função de transferência teórica para as frequências mais altas

    # Plotar o diagrama de magnitude de Bode da função de transferência
    plt.figure(figsize=(10, 6))

    # Plotar a função de transferência teórica

    # Adicionar os pontos experimentais
    plt.plot(x, y, color='red', linestyle='--', marker='o', label=label1)
    plt.plot(x, z, color='orange', linestyle='--', marker='o', label=label2)
    plt.plot(x, w, color='green', linestyle='--', marker='o', label=label3)
    plt.plot(x, k, color='blue', linestyle='--', marker='o', label=label4)


    # Configurar o gráfico
    plt.xlabel('Bits b4b3b2b1 - [1111;0000]')  # Define o rótulo do eixo x
    plt.xticks(x, [f'{bin(val)[2:].zfill(4)}' for val in x[::-1]], rotation=45)  # Inverte a ordem e formata os rótulos
    plt.ylabel('Tensão (V)')
    plt.title(title)
    plt.grid(True)
    plt.legend()

    plt.xlim(xinf, xsup)
    plt.ylim(yinf, ysup)
    plt.show()

#grafico

x = list(range(16))  

y = [-6.3671875,
-5.7421875,
-5.5859375,
-4.9609375,
-4.7265625,
-4.1015625,
-3.9453125,
-3.3203125,
-3.046875,
-2.421875,
-2.265625,
-1.640625,
-1.40625,
-0.78125,
-0.625,
0]
z = [-6.40625,
-6.09375,
-5.15625,
-4.84375,
-4.84375,
-4.53125,
-3.59375,
-3.28125,
-3.125,
-2.8125,
-1.875,
-1.5625,
-1.5625,
-1.25,
-0.3125,
0]

w = [-6.5625,
-6.25,
-5.9375,
-5.625,
-4.0625,
-3.75,
-3.4375,
-3.125,
-3.4375,
-3.125,
-2.8125,
-2.5,
-0.9375,
-0.625,
-0.3125,
0]
k=[-7.1875,
-6.875,
-6.5625,
-6.25,
-5.9375,
-5.625,
-5.3125,
-5,
-2.1875,
-1.875,
-1.5625,
-1.25,
-0.9375,
-0.625,
-0.3125,
0]

print(len(y))

print(len(z))
print(len(w))

print(len(k))


plot(x,y,z,w,k,-0.3,16.1,-7.35,0.1,"Onda de saída (V0)","Pontos teóricos para R1=R","Pontos teóricos para R2=R","Pontos teóricos para R3=R" ,"Pontos teóricos para R4=R")
