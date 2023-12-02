import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction
from scipy.signal import bode


def convert_to_rad(frequencias):
    #return [2 * np.pi * f -2500 for f in frequencias]
    return [2 * np.pi * f for f in frequencias]



def convert_to_db(voltagens):
    #return [20 * np.log10(V/2)-1.5 for V in voltagens]
    return [20 * np.log10(V/2) for V in voltagens]


def plot(w,db,numerator,denominator,xinf,xsup,yinf,ysup,title,label1,label2):
# Criar a função de transferência
    sys = TransferFunction(numerator, denominator)

    # Calcular a magnitude e a fase da resposta em frequência da função de transferência
    w_response, mag_response, _ = bode(sys)

    print(sys)


    w_high = np.logspace(0, 6, num=1000)  # Gera 1000 pontos igualmente espaçados em uma escala logarítmica

    # Calcular os valores da magnitude da função de transferência teórica para as frequências mais altas
    _, mag_response_high, _ = bode(sys, w_high)

    # Plotar o diagrama de magnitude de Bode da função de transferência
    plt.figure(figsize=(10, 6))

    # Plotar a função de transferência teórica
    plt.semilogx(w_high, mag_response_high, label=label1)

    # Adicionar os pontos experimentais
    plt.plot(w, db, color='brown', linestyle='--', marker='o', label=label2)
    # Configurar o gráfico
    plt.xlabel('Frequência (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.title(title)
    plt.grid(True)
    plt.legend()

    plt.xlim(xinf, xsup)
    plt.ylim(yinf, ysup)
    plt.show()


#-------------------------PASSA-ALTO---------------------------


# Dados experimentais
frequencias = [10, 500, 1000, 2000, 3375, 4000, 4500, 5000, 5500, 6000, 6500, 10000, 20000, 21276, 30000, 50000, 70000, 100000]
voltagens = [0.04, 0.06, 0.17, 0.65, 1.89, 2.37, 2.61, 2.65, 2.69, 2.69, 2.65, 2.5, 2.49, 2.49, 2.57, 2.81, 3.22, 3.9]


w = convert_to_rad(frequencias)
db = convert_to_db(voltagens)


# Definir os coeficientes da função de transferência
numerator = [1,0,0]
denominator = [1, 2.128e4, 4.527e8]
label1 = '|T1(s)|'
label2 = 'Pontos Experimentais'
title = '|T1(s)| em comparação com os pontos experimentais'
plot (w,db,numerator,denominator,10,1000000,-40,20,title,label1,label2)


#-------------------------PASSA-BANDA---------------------------

# Lista de valores x
frequencias1 = [100, 500, 1000, 2000, 2490, 3000, 3500, 4000, 4250, 4500, 5000, 6300, 7500, 10000, 20000, 30000, 100000]


# Lista de valores y
voltagens1 = [0.07, 0.3, 0.62, 1.35, 1.73, 2.13, 2.41, 2.45, 2.45, 2.41, 2.25, 1.73, 1.45, 1.07, 0.51, 0.35, 0.145]

w1 = convert_to_rad(frequencias1)
db1 = convert_to_db(voltagens1)
# Definir os coeficientes da função de transferência
numerator1 = [0, 2.128e4, 0]
denominator1 = [1, 2.128e4, 4.527e8]
label1 = '|T2(s)|'
label2 = 'Pontos Experimentais'
title = '|T2(s)| em comparação com os pontos experimentais'
plot (w1,db1,numerator1,denominator1,500,1000000,-40,20,title,label1,label2)



#-------------------------PASSA-BAIXO---------------------------

frequencias2 = [10, 100, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4700, 5000, 6500, 7500, 8500, 10000, 20000, 100000]

# Lista de valores y
voltagens2 = [2.33, 2.33, 2.37, 2.37, 2.41, 2.49, 2.61, 2.69, 2.69, 2.61, 2.37, 1.93, 1.69, 1.03, 0.76, 0.6, 0.44, 0.4, 0.08]

w2 = convert_to_rad(frequencias2)
db2 = convert_to_db(voltagens2)
# Definir os coeficientes da função de transferência
numerator2 = [0,0, 4.527e8]
denominator2= [1, 2.128e4, 4.527e8]
label1 = '|T3(s)|'
label2 = 'Pontos Experimentais'
title = '|T3(s)| em comparação com os pontos experimentais'
plot (w2,db2,numerator2,denominator2,10,1000000,-40,20,title,label1,label2)





#-------------------------PASSA-BAIXO---------------------------

# Lista de valores x
frequencias1 = [100,
500,
1000,
2300,
2500,
3500,
4000,
4200,
4500,
5000,
6000,
6200,
10000,
20000,
100000]

# Lista de valores y
voltagens1 = [0.08,
0.55,
0.55,
1.43,
1.55,
2.13,
2.17,
2.13,
2.09,
1.87,
1.57,
1.53,
0.9,
0.42,
0.09]
w1 = convert_to_rad(frequencias1)
db1 = convert_to_db(voltagens1)
# Definir os coeficientes da função de transferência
numerator1 = [0, -2.128e4, 0]
denominator1 = [1, 2.128e4, 4.527e8]
label1 = '|T1(s)|'
label2 = 'Pontos Experimentais'
title = '|T1(s)| em comparação com os pontos experimentais'
plot (w1,db1,numerator1,denominator1,500,1000000,-40,20,title,label1,label2)



#-------------------------PASSA-BAIXO---------------------------

frequencias2 = [
    100,
1000,
2000,
2500,
2800,
3000,
3200,
3500,
4000,
4500,
4550,
5000,
10000,
20000,
50000,
100000
]

# Lista de valores y
voltagens2 = [2.17,
2.25,
2.41,
2.49,
2.49,
2.49,
2.45,
2.37,
2.09,
1.77,
1.73,
1.51,
0.35,
0.1,
0.04,
0.03]

w2 = convert_to_rad(frequencias2)
db2 = convert_to_db(voltagens2)
# Definir os coeficientes da função de transferência
numerator2 = [0,0, 4.527e8]
denominator2= [1, 2.128e4, 4.527e8]
label1 = '|T2(s)|'
label2 = 'Pontos Experimentais'
title = '|T2(s)| em comparação com os pontos experimentais'
plot (w2,db2,numerator2,denominator2,500,1000000,-40,20,title,label1,label2)

#-------------------------PASSA-BANDA---------------------------

# Dados experimentais
frequencias = [100,
1000,
2000,
2500,
2800,
3000,
3200,
3500,
4000,
4500,
4550,
4600,
5000,
10000,
50000,
100000,
1000000]
voltagens = [2.13,
2.25,
2.41,
2.49,
2.49,
2.49,
2.49,
2.37,
2.13,
1.79,
1.77,
1.73,
1.53,
0.38,
0.13,
0.21,
0.09]


w = convert_to_rad(frequencias)
db = convert_to_db(voltagens)


# Definir os coeficientes da função de transferência
numerator = [0,0,-4.527e8]
denominator = [1, 2.128e4, 4.527e8]
label1 = '|T3(s)|'
label2 = 'Pontos Experimentais'
title = '|T3(s)| em comparação com os pontos experimentais'
plot (w,db,numerator,denominator,500,1000000,-40,20,title,label1,label2)

