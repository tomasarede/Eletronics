import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction
from scipy.signal import bode



def plot(x, y, z, xinf, xsup, yinf, ysup, title, label1, label2, ):
    # Calcular os valores da magnitude da função de transferência teórica para as frequências mais altas

    # Plotar o diagrama de magnitude de Bode da função de transferência
    plt.figure(figsize=(10, 6))

    # Plotar a função de transferência teórica

    # Adicionar os pontos experimentais
    plt.plot(x, y, color='red', linestyle='--', marker='o', label=label1)
    plt.plot(x, z, color='blue', linestyle='--', marker='o', label=label2)


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

y = [
-3.125,
-2.91666666666667,
-2.70833333333333,
-2.5,
-2.29166666666667,
-2.08333333333333,
-1.875,
-1.66666666666667,
-1.45833333333333,
-1.25,
-1.04166666666667,
-0.833333333333333,
-0.625,
-0.416666666666667,
-0.208333333333333,
0]

z = [-6.25,
-5.83333333333333,
-5.41666666666667,
-5,
-4.58333333333333,
-4.16666666666667,
-3.75,
-3.33333333333333,
-2.91666666666667,
-2.5,
-2.08333333333333,
-1.66666666666667,
-1.25,
-0.833333333333333,
-0.416666666666667,
0]



plot(x,y,z,-0.2,16.2,-6.40,0.1,"Onda de saída (V0)","Pontos teóricos para Rf=2R", "Pontos teóricos para Rf=4R")
