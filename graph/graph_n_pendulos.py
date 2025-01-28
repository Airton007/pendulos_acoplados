"""
    Programa para os gráficos para o caso de N>2 pêndulos
"""
#> partes separadas por #%% podem ser executadas separadamente num kernel jupyter
#%%
import numpy as np 
import matplotlib.pyplot as plt

# Seleciona o arquivo de interesse
file_path = 'data/pend_acop_pos_diferentes.dat' # Alterar para o arquivo desejado
# Carregar os dados do arquivo
try:
    data = np.loadtxt(file_path)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    exit()

# Verificar se os dados têm pelo menos 3 colunas (tempo, posição e velocidade de pelo menos 1 pêndulo)
if data.shape[1] < 3:
    print("Erro: O arquivo deve conter pelo menos colunas para tempo, posição e velocidade.")
    exit()

# Identificar o número de pêndulos
time = data[:, 0]  # Primeira coluna é o tempo
num_columns = data.shape[1]
num_pendulums = (num_columns - 1) // 2  # Número de pêndulos
if num_pendulums * 2 + 1 != num_columns:
    print("Erro: O número de colunas no arquivo não corresponde ao formato esperado (tempo, posições, velocidades).")
    exit()

#%%
# Separar posições e velocidades
x_j = data[:, 1:num_pendulums + 1]
v_j = data[:, num_pendulums + 1:]
# Coordenada normal do centro de massa
q_1 = x_j[:, :].sum(axis=1)
p_1 = v_j[:, :].sum(axis=1)

#%%
#> Plot das coordenadas dos pêndulos
fig, ax = plt.subplots( nrows=4 , ncols=1 , figsize=( 12 , 18 ) )
ax = ax.flatten()
for i in range(num_pendulums):
    ax[0].plot(time, x_j[:, i]/x_j[:, i].max() , label=f'Pêndulo {i + 1}')
ax[0].legend( fontsize=12 )
for i in range(num_pendulums):
    ax[1].plot(time, v_j[:, i], label=f'Pêndulo {i + 1}')
ax[1].legend( fontsize=12 )
ax[2].plot( time , q_1/q_1.max() , color='limegreen' )
ax[3].plot( time , p_1/p_1.max() , color='firebrick' )
ax[0].grid( )
ax[1].grid( )
ax[2].grid( )
ax[3].grid( )
ax[3].set_xlabel('Tempo [u.a.]' , fontsize=14 )
ax[0].set_ylabel('Coordenadas naturais [u.a.]' , fontsize=14 ) ; ax[0].set_title('Coordenadas naturais' , fontsize=14 )
ax[1].set_ylabel('Velocidades naturais [u.a.]' , fontsize=14 ) ; ax[1].set_title('Velocidades naturais' , fontsize=14 )
ax[2].set_ylabel('Coordenada normal [u.a.]' , fontsize=14 ) ; ax[2].set_title('Coordenada normal do centro de massa' , fontsize=14 )
ax[3].set_ylabel('Velocidade normal [u.a.]' , fontsize=14 ) ; ax[3].set_title('Velocidade da coordenada normal do centro de massa' , fontsize=14 )
fig.savefig( 'rel/graph_coordenadas_pendulos.pdf' , dpi=300 , bbox_inches='tight' )
