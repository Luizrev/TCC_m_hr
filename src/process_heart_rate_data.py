# Importamos as bibliotecas Pandas e os para manipulação de dados e arquivos.
import pandas as pd
import os

# Criamos listas vazias para armazenar os dados de identificação, tempo e batimentos cardíacos
# por minuto (BPM).
ident = []
time = []
bpm = []

# Definimos o caminho da pasta onde os arquivos de texto estão localizados e o nome do arquivo
# CSV que será gerado.
pasta_l = 'C:/Users/rev3r/Desktop/TCC_m_hr/data/heartrate'
pasta_s = 'C:/Users/rev3r/Desktop/TCC_m_hr/results'
nome_csv = 'heartrate.csv'

# Percorremos todos os arquivos de texto na pasta, extraindo o identificador, o tempo e os valores
# de batimentos cardíacos por minuto (BPM), armazenando-os nas listas correspondentes.

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
                time.append(i[1][:aux.index(',')])
                bpm.append(i[1][aux.index(',')+1:-1])

# Criamos um DataFrame com os dados processados e salvamos em um arquivo CSV.
dados = {'id': ident, 'time': time, 'bpm': bpm}
df_bpm = pd.DataFrame(dados)
caminho_para_salvar = os.path.join(pasta_s, nome_csv)
df_bpm.to_csv(caminho_para_salvar, index=False)
