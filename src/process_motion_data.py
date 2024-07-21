# Importamos as bibliotecas Pandas e os para manipulação de dados e arquivos.
import pandas as pd
import os

# A função indice_aux é usada para encontrar a posição de um caractere específico em uma
# string, permitindo identificar a posição de espaços em branco no texto
def indice_aux(texto, caractere, n):
    indice = -1
    for _ in range(n):
        indice = texto.find(caractere, indice + 1)
        if indice == -1:
            break
    return indice

# Criamos listas vazias para armazenar os dados de identificação, tempo e aceleração nos eixos x,
# y e z.
ident = []
time = []
x_ace = []
y_ace = []
z_ace = []

# Definimos o caminho da pasta onde os arquivos de texto estão localizados e o nome do arquivo
# CSV que será gerado.
pasta_l = 'C:/Users/rev3r/Desktop/TCC_m_hr/data/motion'
pasta_s = 'C:/Users/rev3r/Desktop/TCC_m_hr/results'
nome_csv = 'motion.csv'

# Percorremos todos os arquivos de texto na pasta, extraindo o identificador, o tempo e os valores
# de aceleração nos eixos x, y e z, armazenando-os nas listas correspondentes.
for nome in os.listdir(pasta_l):
    if nome.endswith('.txt'):
        caminho_temp = os.path.join(pasta_l, nome)
        with open(caminho_temp, 'r') as arquivo:
            idt = nome[:nome.index('_')]
            content = arquivo.readlines()
            cont_sep = enumerate(content)
            for i in cont_sep:
                aux = i[1]
                ident.append(idt)
                time.append(i[1][:aux.index(' ')])
                x_ace.append(i[1][aux.index(' ')+1:indice_aux(i[1], ' ', 2)])
                y_ace.append(i[1][indice_aux(i[1], ' ', 2)+1:indice_aux(i[1], ' ', 3)])
                z_ace.append(i[1][indice_aux(i[1], ' ', 3)+1:-1])

# Criamos um DataFrame com os dados processados e salvamos em um arquivo CSV.
print("salvando...")     
dados = {'id': ident, 'time': time, 'x': x_ace, 'y': y_ace, 'z': z_ace}
df_bpm = pd.DataFrame(dados)
caminho_para_salvar = os.path.join(pasta_s, nome_csv)
df_bpm.to_csv(caminho_para_salvar, index=False)
