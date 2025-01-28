
# Simulação de Pêndulos Acoplados

Este projeto implementa uma simulação numérica do movimento de um sistema de **N pêndulos acoplados**. As equações diferenciais do sistema são resolvidas usando o método de Runge-Kutta de quarta ordem (RK4). A saída do programa contém os resultados da simulação, que podem ser analisados para estudar o comportamento dinâmico do sistema.

## Estrutura dos Códigos

O projeto é composto pelos seguintes componentes principais:

1. **Arquivo Principal (`osc_acopladas_n`)**:
   - Configura e executa a simulação.
   - Solicita ao usuário o número de pêndulos e as condições iniciais.
   - Salva os resultados em arquivos de saída.

2. **Módulo `runge_kutta`**:
   - Implementa o método RK4 para a integração numérica das equações diferenciais.

3. **Arquivos geradores de gráficos (`graph_2_pendulos.py` e `graph_n_pendulos.py`)**:
   - O arquivo `graph_2_pendulos.py` faz a leitura dos arquivos `.dat` gerados pela simulação do código `osc_acopladas_n`, que contêm as colunas com tempo, posições e velocidades dos dois pêndulos. Para diferentes condições iniciais (iguais, opostas e diferentes), são gerados os gráficos correspondentes, salvos em arquivos PDF.
   
   As funções geradas para plotagem são:
   - `plot_coordenadas`: Plota as coordenadas naturais e normais (posições e velocidades).
   - `plot_espaço_de_fase`: Gera os gráficos no espaço de fase para diferentes coordenadas.
   - `plot_energia`: Mostra a conservação e a transmissão de energia entre os dois pêndulos.
Para mais detalhes sobre os gráficos gerados, consulte o arquivo `README.md` no diretório [`\.graph`](./.graph/README.md).

### Configurações do Sistema

#### Parâmetros Fixos
- **Massa (m):** 10.0 kg
- **Constante elástica (k):** 10.0 N/m
- **Gravidade (g):** 1000.0m/s²
- **Comprimento da corda (l):** 1.0 m
- **Passo de tempo (h):** 0.001 s
- **Número de passos (N):** 10.000

#### Parâmetros Modificáveis
Os parâmetros físicos podem ser alterados diretamente no código, por exemplo:

```fortran
real(kind=dp), parameter :: m = 1.0_dp, k = 10.0_dp, g = 1000.0_dp, l = 1.0_dp
```

### Frequência Natural
A frequência natural do sistema é calculada como:

$$
\omega_0 = \sqrt{\frac{g}{l}}
$$

### Dimensão do Sistema
A dimensão \(d\) do sistema é o dobro do número de pêndulos \(N\), pois inclui posições e velocidades:

$$
d = 2\times N
$$

## Entradas do Usuário
1. **Número de pêndulos (N):** Deve ser pelo menos 2. Caso a opção de escolha seja 1, aparecerá uma mensagem de "opção inválida".
2. **Condições iniciais:**
   - **1:** Todas as posições iguais (Movimento Harmônico Simples do centro de massa).
   - **2:** Posições alternadas (opostas) (Movimento Harmônico Simples das posições relativas).
   - **3:** Posições diferentes (configuração arbitrária).

## Saída

Os resultados da simulação são armazenados em arquivos no diretório `data/`. Os nomes dos arquivos dependem das condições iniciais selecionadas:

- `pend_acop_pos_iguais.dat`
- `pend_acop_pos_opostas.dat`
- `pend_acop_pos_diferentes.dat`

Para o caso de \(N = 2\), os resultados são salvos no subdiretório `data/2/`.

Cada arquivo contém:
- **Tempo (t):** Instante de tempo da simulação.
- **Posições e velocidades (z):** Estados do sistema no instante \(t\).

## Métodos Numéricos

### Método de Runge-Kutta de Quarta Ordem (RK4)
O RK4 é usado para integrar as equações diferenciais do sistema. O método calcula os coeficientes intermediários \(k_1, k_2, k_3, k_4\) e combina-os para estimar o próximo estado:

$$
\mathbf{z}_{i+1} = \mathbf{z}_i + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

Os coeficientes são calculados como:

$$
\begin{aligned}
k_1 &= h \cdot g(t_i, \mathbf{z}_i) \\
k_2 &= h \cdot g(t_i + \frac{h}{2}, \mathbf{z}_i + \frac{k_1}{2}) \\
k_3 &= h \cdot g(t_i + \frac{h}{2}, \mathbf{z}_i + \frac{k_2}{2}) \\
k_4 &= h \cdot g(t_i + h, \mathbf{z}_i + k_3)
\end{aligned}
$$

## Exemplos de Execução

### Modo Manual
Neste modo, o usuário fornece os parâmetros diretamente no terminal.

#### Exemplo de Execução
Entrada:
```bash
Digite o número de pêndulos acoplados (N):
3
Escolha as condições iniciais:
1. Todas as posições iguais - MHS do centro de massa
2. Posições alternadas (opostas) - MHS das posições relativas
3. Posições diferentes
1
```

Saída:
```bash
Arquivo de saída: data/pend_acop_pos_iguais.dat
```

O arquivo gerado conterá:
```
0.000000    1.000000    1.000000    1.000000    0.000000    0.000000    0.000000
0.001000    0.999950    1.000000    1.000050    0.000000    0.000001    -0.000001
...
```

### Modo Arquivo
Os dados de entrada são lidos de um arquivo de configuração (exemplo: `config.dat`).

#### Formato de Arquivo (`config.dat`):
```
3  ! Número de pêndulos
1  ! Condições iniciais
```

#### Execução:
```bash
./osc_acopladas_n < config.dat
```

Saída:
```bash
Arquivo de saída: data/pend_acop_pos_iguais.dat
```
## Reutilização do Código

### Incorporar a Biblioteca RK4 em Outros Projetos
1. Copie o módulo `runge_kutta.f90` para seu projeto.
2. Use o módulo no código principal:
   ```fortran
   use runge_kutta
   ```
3. Defina uma função de derivadas específica para o novo sistema e utilize `rk4_multi` para realizar a integração.

### Adicionar Novos Recursos
- **Condições iniciais personalizadas:** Adicione novas opções no menu de entrada para simular diferentes configurações iniciais.
- **Plotagem:** Integre scripts em Python ou Gnuplot para visualizar os resultados da simulação diretamente.

## Observações

Certifique-se de que o diretório `data/` exista antes de executar o programa. Caso contrário, crie-o para evitar erros de saída:

```bash
mkdir -p data/2
```
