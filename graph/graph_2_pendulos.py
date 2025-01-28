"""
    Programa para a análise gráfica para o caso de dois pêndulos
"""
#> partes separadas por #%% podem ser executadas separadamente num kernel jupyter
#%%
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos dados
data_file_iguais = 'data/2/pend_acop_pos_iguais.dat'
data_file_opostas  = 'data/2/pend_acop_pos_opostas.dat'
data_file_diferentes = 'data/2/pend_acop_pos_diferentes.dat'

# Carregar os dados dos arquivos
try:
    data_iguais = np.loadtxt(data_file_iguais)
    data_opostas = np.loadtxt(data_file_opostas)
    data_diferentes = np.loadtxt(data_file_diferentes)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    exit()

#> Verificar se os arquivos têm todos 5 colunas
if data_iguais.shape[1] != 5:
    print("Erro: O arquivo "+data_iguais+" deve conter cinco colunas para tempo, posição e velocidade.")
    exit()
if data_diferentes.shape[1] != 5:
    print("Erro: O arquivo "+data_diferentes+" deve conter cinco colunas para tempo, posição e velocidade.")
    exit()
if data_opostas.shape[1] != 5:
    print("Erro: O arquivo "+data_opostas+" deve conter cinco colunas para tempo, posição e velocidade.")
    exit()

#%%
#> Funções para os plots
def plot_coordenadas( data , file_path ):
    """
    Função que recebe o conjunto de dados de interesse e plota os gráficos das coordenadas

    Args:
        data =: conjunto de dados de interesse
        file_path =: caminho da imagem gerada + extensão

    Retorna:
        Não retorna nenhuma variável, apenas padroniza uma subrotina para plotar os gráficos das coordenadas    
    """
    time = data[:, 0]  # Primeira coluna é o tempo
    x_1 = data[ :, 1 ] ; v_1 = data[ :, 3 ]
    x_1_max = x_1.max() ; v_1_max = v_1.max()
    x_2 = data[ :, 2 ] ; v_2 = data[ :, 4 ]
    x_2_max = x_1.max() ; v_2_max = v_1.max()
    q_1 = x_1 + x_2 ; vq1 = v_1 + v_2
    q_2 = x_1 - x_2 ; vq2 = v_1 - v_2
    fig, ax = plt.subplots( nrows=4 , ncols=1 , figsize=( 12, 18 ) ) 
    ax = ax.flatten() # Transforma o ax em um array 1D para facilitar
    ax[0].plot( time , x_1/x_1_max , label=r'$x_1$' , color='blue' )
    ax[0].plot( time , x_2/x_2_max , '--' , label=r'$x_2$' , color='orange' )
    ax[0].legend( fontsize=12 )
    ax[1].plot( time , v_1/v_1_max , label=r'$\dot{x}_1$' , color='blue' )
    ax[1].plot( time , v_2/v_2_max , '--' , label=r'$\dot{x}_2$' , color='orange' )
    ax[1].legend( fontsize=12 )
    ax[2].plot( time , q_1/q_1.max() , label=r'$q_1$' , color='limegreen' )     
    ax[2].plot( time , q_2/q_2.max() , '--' , label=r'$q_2$' , color='firebrick' )
    ax[2].legend( fontsize=12 )
    ax[3].plot( time , vq1/vq1.max() , label=r'$\dot{q}_1$' , color='limegreen' ) 
    ax[3].plot( time , vq2/vq2.max() , '--' , label=r'$\dot{q}_2$' , color='firebrick' )
    ax[3].legend( fontsize=12 )
    ax[0].grid( )
    ax[1].grid( )
    ax[2].grid( )
    ax[3].grid( )
    ax[3].set_xlabel('Tempo [u.a.]' , fontsize=14 )
    ax[0].set_ylabel('Coordenadas naturais [u.a.]' , fontsize=14 ) ; ax[0].set_title('Coordenadas naturais' , fontsize=14 )
    ax[1].set_ylabel('Velocidades naturais [u.a.]' , fontsize=14 ) ; ax[1].set_title('Velocidades naturais' , fontsize=14 )
    ax[2].set_ylabel('Coordenadas normais [u.a.]' , fontsize=14 ) ; ax[2].set_title('Coordenadas normais' , fontsize=14 )
    ax[3].set_ylabel('Velocidades normais [u.a.]' , fontsize=14 ) ; ax[3].set_title('Velocidades normais' , fontsize=14 )
    fig.savefig( file_path , dpi=300 , bbox_inches='tight' )

def plot_espaço_de_fase( data , file_path ):
    """
    Função que recebe o conjunto de dados de interesse e plota os perfis do espaço de fase

    Args:
        data =: conjunto de dados de interesse
        file_path =: caminho da imagem gerada + extensão

    Retorna:
        Não retorna nenhuma variável, apenas padroniza uma subrotina para plotar os perfis do espaço de fase
    """
    x_1 = data[ :, 1 ] ; v_1 = data[ :, 3 ]
    x_1_max = x_1.max() ; v_1_max = v_1.max()
    x_2 = data[ :, 2 ] ; v_2 = data[ :, 4 ]
    x_2_max = x_1.max() ; v_2_max = v_1.max()
    q_1 = x_1 + x_2 ; vq1 = v_1 + v_2
    q_2 = x_1 - x_2 ; vq2 = v_1 - v_2
    fig, ax = plt.subplots( nrows=2 , ncols=2 , figsize=( 12, 12 ) ) 
    ax = ax.flatten()
    ax[0].plot( x_1/x_1_max , v_1/v_1_max , color='blue' )
    ax[1].plot( x_2/x_2_max , v_2/v_2_max , color='orange' )
    ax[2].plot( q_1/q_1.max() , vq1/vq1.max() , color='limegreen' )
    ax[3].plot( q_2/q_2.max() , vq2/vq2.max() , color='firebrick' )
    ax[0].grid( )
    ax[1].grid( )
    ax[2].grid( )
    ax[3].grid( )
    ax[3].set_xlabel('Tempo [u.a.]' , fontsize=14 )
    ax[0].set_title(f'Coordenada $x_1$' , fontsize=14 )
    ax[1].set_title(f'Coordenada $x_2$' , fontsize=14 )
    ax[2].set_title(f'Coordenada $q_1$' , fontsize=14 )
    ax[3].set_title(f'Coordenada $q_2$' , fontsize=14 )
    fig.savefig( file_path , dpi=300 , bbox_inches='tight' )

def plot_energia( data , file_path ):
    """
    Função que recebe o conjunto de dados de interesse e plota o gráfico da energia

    Args:
        data =: conjunto de dados de interesse
        file_path =: caminho da imagem gerada + extensão

    Retorna:
        Não retorna nenhuma variável, apenas padroniza uma subrotina para plotar o gráfico da energia
    """
    time = data[:, 0] 
    x_1 = data[ :, 1 ] ; v_1 = data[ :, 3 ]
    x_2 = data[ :, 2 ] ; v_2 = data[ :, 4 ]
    # As constantes abaixo são cópias das usadas no programa que gera os dados
    y_1 = 10 - np.sqrt(100-x_1**2)
    y_2 = 10 - np.sqrt(100-x_2**2)
    U = (x_2-x_1)**2
    E_1 = 0.5*10*U + 1000*y_1 + 0.5*v_1**2
    E_2 = 0.5*10*U + 1000*y_2 + 0.5*v_2**2
    E_T = 0.5*10*U + 1000*y_2 + 0.5*v_2**2+ 1000*y_1 + 0.5*v_1**2
    E_T = E_T/E_T.max()
    E_1 = E_1/E_1.max()
    E_2 = E_2/E_2.max()
    fig, ax = plt.subplots( nrows=1 , ncols=1 , figsize=( 12, 4.5 ) ) 
    ax.plot( time , E_1 , color='blue' , label='Partícula 1' )
    ax.plot( time , E_2 , '--' , color='orange' , label='Partícula 2' )
    ax.plot( time , E_T , color='#e91e63' , label='Total' )
    ax.legend( fontsize=12 )
    ax.grid( )
    ax.set_xlabel( 'Tempo [u.a.]' , fontsize=14 )
    ax.set_ylabel( 'Energia [u.a.]' , fontsize=14 ) 
    ax.set_title(f'Energia do sistema' , fontsize=14 )
    fig.savefig( file_path , dpi=300 , bbox_inches='tight' )

#%%
#> Caso das posições iniciais iguais
plot_coordenadas( data_iguais , 'rel/graph_coordenadas_iguais.pdf' )

#%%
#> Caso das posições iniciais opostas
plot_coordenadas( data_opostas , 'rel/graph_coordenadas_opostas.pdf')

# %%
#> Caso das posições iniciais diferentes
plot_coordenadas( data_diferentes , 'rel/graph_coordenadas_diferentes.pdf' )
# Para esse caso vale a pena olhar para o espaço de fase das coordenadas
plot_espaço_de_fase( data_diferentes , 'rel/graph_espaços_de_fase.pdf' )
# Conservação da energia e transmissão de energia de um para outro pêndulo
plot_energia( data_diferentes , 'rel/graph_energia.pdf' )
