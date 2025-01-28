# Análise Gráfica de Pêndulos Acoplados

Este repositório contém dois scripts, `graph_2_pendulos.py` e `graph_n_pendulos.py`, com extensão em Python e são importante 
para a análise gráfica do comportamento dinâmico de **pêndulos acoplados**,tanto para o caso de dois pêndulos quanto para 
sistemas com **N pêndulos**. Utilizam dados previamente gerados pelo  programa principal, `pend_acoplad.f90` e permitem 
explorar as características como coordenadas e velocidades naturais e normais, perfis de fase no espaço e a conservação de 
energia do sistema.


- **Scripts principais**:
  - **`graph_2_pendulos.py`**: Script para o caso com dois pêndulos acoplados.
  - **`graph_n_pendulos.py`**: Script para o caso com N pêndulos acoplados.

## Requisitos

Certifique-se de que as seguintes bibliotecas estão instaladas:
- `numpy`
- `matplotlib`

Instale as dependências com:
```bash
!pip install numpy
```
```bash
!pip install matplotlib
```

## Funcionalidades

### 1. Caso com dois pêndulos (`analise_pendulos_2.py`)

**Entrada**: Arquivos de dados com 5 colunas (tempo, posições e velocidades de dois pêndulos).

**Gráficos gerados**:
- Coordenadas naturais e normais.
- Velocidades naturais e normais.
- Espaço de fase (coordenadas versus velocidades).
- Energia do sistema e transferência de energia entre os pêndulos.

### 2. Caso com N pêndulos (`analise_pendulos_n.py`)

**Entrada**: Arquivos de dados com pelo menos 3 colunas (tempo, posições e velocidades de N pêndulos).

**Gráficos gerados**:
- Coordenadas naturais (posições de cada pêndulo).
- Velocidades naturais.
- Coordenada normal do centro de massa.
- Velocidade normal associada ao centro de massa.


## Formato dos Arquivos de Dados

Os arquivos de dados devem ser estruturados como:

```
tempo  posição_1  posição_2  ...  velocidade_1  velocidade_2  ...
```

- Para o caso de dois pêndulos, são esperadas 5 colunas.
- Para o caso de N pêndulos, o número de colunas deve ser `2N + 1`.

---

## Como Executar

Execute o script correspondente:

### Para dois pêndulos:
```bash
python graph_2_pendulos.py
```

### Para N pêndulos:
```bash
python graph_n_pendulos.py
```

### Modifique o arquivo de entrada:

No início dos scripts, caso ache interessante altere o caminho do arquivo para o dataset desejado:

### Resultados:

Os gráficos serão gerados no diretório `rel/` com extensão `.pdf`.

## Observações

- Certifique-se de que os arquivos de dados estão devidamente formatados. Erros no formato resultarão na interrupção da execução.
- Os gráficos possuem legendas e escalas automáticas, mas é possível ajustá-las nos scripts para maior personalização.
