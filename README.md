# Space Shooter com Pygame

Jogo de tiro espacial desenvolvido em Python com a biblioteca Pygame. O jogador controla uma nave, dispara contra asteroides resistentes e precisa sobreviver aos impactos enquanto acumula pontos.

O projeto foi desenvolvido com foco na aplicação prática de Programação Orientada a Objetos, organização em classes, tratamento de eventos, detecção de colisões, atualização de estados e renderização em tempo real.

## Funcionalidades

- Movimentação horizontal da nave com limitação nas bordas da tela;
- Disparos independentes e remoção automática ao saírem da área visível;
- Asteroide com posição, velocidade e sentido de rotação aleatórios;
- Detecção de colisão entre tiro e asteroide;
- Detecção de colisão entre asteroide e nave;
- Sistema de pontuação;
- Sistema de três vidas;
- Game Over com reinício da partida;
- Dano visual progressivo na nave;
- Nave personalizada com asas, cabine, motores e propulsores animados;
- Asteroide irregular com crateras, contorno e rotação;
- Barra de resistência e dano progressivo no asteroide;
- Execução a 60 FPS.

## Controles

| Ação | Teclas |
| --- | --- |
| Mover para a esquerda | `A` ou `←` |
| Mover para a direita | `D` ou `→` |
| Disparar | `Espaço` |
| Reiniciar após o Game Over | `R` |
| Encerrar | Fechar a janela |

## Regras do jogo

- A nave começa com três vidas.
- Cada colisão direta com o asteroide remove uma vida.
- A aparência da nave muda conforme o dano recebido.
- O asteroide possui três pontos de resistência.
- Cada disparo retira um ponto de resistência do asteroide.
- A pontuação aumenta quando o asteroide é completamente destruído.
- O asteroide muda de cor, recebe rachaduras e perde parte da barra de resistência conforme é atingido.
- Ao perder todas as vidas, a partida entra no estado de Game Over.
- Pressionar `R` restaura a nave, as vidas, a pontuação e o asteroide.

## Tecnologias utilizadas

- Python 3;
- Pygame 2.6.1;
- Biblioteca padrão `random`;
- Biblioteca padrão `math`;
- Git e GitHub para versionamento.

O projeto foi desenvolvido e testado com Python 3.13.15 e Pygame 2.6.1.

## Estrutura do projeto

| Arquivo | Responsabilidade |
| --- | --- |
| `Main.py` | Inicializa o Pygame, controla o game loop, os eventos, as colisões, a pontuação, as vidas e o Game Over. |
| `ElementoJogo.py` | Classe base que reúne atributos comuns, como posição, dimensões, cor e velocidade. |
| `Nave.py` | Controla a movimentação, os disparos, a atualização dos tiros e o desenho da nave. |
| `Asteroid.py` | Controla o surgimento, a movimentação, a rotação, a resistência, o dano e o desenho do asteroide. |
| `requirements.txt` | Informa a dependência que deve ser instalada no ambiente virtual. |

## Pré-requisitos

Antes de iniciar, instale:

- [Python 3](https://www.python.org/downloads/);
- [Git](https://git-scm.com/downloads), caso utilize a clonagem do repositório;
- Uma IDE ou editor, como [Visual Studio Code](https://code.visualstudio.com/) ou PyCharm.

Durante a instalação do Python no Windows, marque a opção **Add Python to PATH**.

## Instalação no Windows com PowerShell

Abra o PowerShell na pasta em que deseja salvar o projeto e execute:

```powershell
git clone <URL_DO_REPOSITORIO>
cd space-shooter-with-pygame
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python Main.py
```

Substitua `<URL_DO_REPOSITORIO>` pela URL HTTPS apresentada no botão **Code** do GitHub.

Se o projeto tiver sido baixado como ZIP, extraia o arquivo, abra o terminal dentro da pasta extraída e comece pelo comando:

```powershell
py -m venv .venv
```

### Caso o PowerShell bloqueie a ativação

Execute esta permissão temporária somente na janela atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Depois continue com:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python Main.py
```

## Instalação no Windows com Prompt de Comando

```bat
git clone <URL_DO_REPOSITORIO>
cd space-shooter-with-pygame
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python Main.py
```

## Instalação no Linux ou macOS

```bash
git clone <URL_DO_REPOSITORIO>
cd space-shooter-with-pygame
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python Main.py
```

## Configuração no Visual Studio Code

Depois de criar o ambiente virtual e instalar as dependências:

1. Abra a pasta do projeto no VS Code:

   ```powershell
   code .
   ```

2. Instale a extensão oficial **Python**, publicada pela Microsoft.
3. Pressione `Ctrl + Shift + P`.
4. Procure por **Python: Select Interpreter**.
5. Selecione o interpretador localizado em `.venv`.
6. Abra um novo terminal integrado e execute:

   ```powershell
   python Main.py
   ```

No Windows, o interpretador normalmente estará em:

```text
.venv\Scripts\python.exe
```

No Linux e no macOS, normalmente estará em:

```text
.venv/bin/python
```

## Executando novamente

Sempre que abrir um novo terminal, ative o ambiente virtual antes de executar o jogo.

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python Main.py
```

No Prompt de Comando:

```bat
.venv\Scripts\activate.bat
python Main.py
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python Main.py
```

## Conceitos de Programação Orientada a Objetos

O projeto demonstra os seguintes conceitos:

- **Herança:** `Nave` e `Asteroid` herdam atributos e comportamentos de `ElementoJogo`.
- **Sobrescrita de métodos:** as subclasses implementam suas próprias versões de `mover()` e `desenhar()`.
- **Polimorfismo:** objetos derivados da mesma classe base apresentam comportamentos visuais e de movimentação diferentes.
- **Encapsulamento:** movimentação, disparos, dano, desenho e reinício são organizados em métodos responsáveis por cada comportamento.
- **Composição:** a classe `Jogo` mantém e coordena objetos das classes `Nave` e `Asteroid`.

## Funcionamento do game loop

Enquanto a partida está aberta, o método principal repete quatro etapas:

1. Limita a execução a 60 FPS;
2. Processa os eventos do teclado e da janela;
3. Atualiza nave, tiros, asteroide e colisões;
4. Desenha o estado atual e apresenta o novo frame.

Durante o Game Over, as atualizações dos elementos são interrompidas, mas o processamento de eventos continua ativo para permitir o reinício com a tecla `R`.

## Solução de problemas

### `ModuleNotFoundError: No module named 'pygame'`

Confirme que o ambiente virtual está ativado e execute:

```powershell
python -m pip install -r requirements.txt
```

### O VS Code continua indicando que o Pygame não está instalado

Selecione o interpretador do ambiente `.venv` em **Python: Select Interpreter** e abra um novo terminal integrado.

Para conferir o interpretador utilizado:

```powershell
python -c "import sys; print(sys.executable)"
```

### Verificar a instalação do Pygame

```powershell
python -c "import pygame; print('Pygame:', pygame.version.ver)"
```

O resultado esperado deve apresentar a versão `2.6.1`.

## Possíveis evoluções

- Inclusão de múltiplos asteroides simultâneos;
- Efeitos sonoros e música de fundo;
- Tela inicial e menu de pausa;
- Recorde de pontuação;
- Fases com dificuldade progressiva;
- Diferentes tipos de inimigos e disparos;
- Uso de imagens e sprites externos.

---

Desenvolvido por Laura Reded, Mariana Kleina, Maiara Wojciekovski e Otavio Wenzel como projeto acadêmico em Python e Pygame em Tópicos Especiais na Universidade Positivo.