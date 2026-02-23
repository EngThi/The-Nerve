> *Disclaimer: Inicialmente, eu estava usando apenas a plataforma do Blueprint para documentar o progresso (não sabia que os registros precisavam estar no repositório também). Estou compilando os registros passados aqui para refletir a verdadeira timeline do projeto.*

# Diário de Desenvolvimento (Journal) - The Nerve

Este documento registra a evolução, as decisões de engenharia e os desafios enfrentados durante o desenvolvimento do **The Nerve V1**, alinhado com as postagens feitas na plataforma do Blueprint.

---

### 10 Fev 2026: I did many things (I MOVED THE PROJECT BACK HERE AGAIN)
**Title: The "Panic" That Became a Feature: Upgrade and Resilience**

O projeto começou como uma tentativa de criar uma interface física para automatizar fluxos de vídeo no `n8n`. Inicialmente, enfrentei um momento de "pânico" com a estrutura do projeto e as ferramentas. Decidi recomeçar o design do zero. Isso acabou sendo crucial: percebi que eu não estava apenas fazendo um "teclado de atalhos", mas sim um controlador modular muito mais robusto.
*Nota: Vou buscar as imagens de rascunhos antigos dessa época para incluir aqui.*

### 12 Fev 2026: Mexi no hardware e uma transição para a Arquitetura Modular
**(Hardware Changes - Log V2)**

A escolha do microcontrolador e a estrutura da placa foram os grandes divisores de águas desta fase.

**1. Pivot do Microcontrolador (RP2040 -> ESP32-S3):**
- O plano original era usar o RP2040. Era barato, mas a falta de conectividade limitaria o escopo para automações presas ao cabo.
- Migrei para o **ESP32-S3 ProS3[D]**. Além do USB HID nativo (essencial para simular periféricos de entrada), o Wi-Fi embutido abriu portas para disparar webhooks HTTP direto para o n8n, sem precisar de scripts no PC.

**2. Modularidade & Manutenção:**
Decidi que nada de interface seria soldado diretamente na placa. Se um encoder quebra, não quero perder a PCB inteira. Implementei conectores universais JST e terminais de parafuso.

**3. Pinout & Voltagem / DFM (Pre não ter que soldar tudo):**
Criar interfaces de 6 pinos para suportar módulos de 3.3V e 5V simultaneamente exigiu refazer grande parte do roteamento lógico no EasyEDA. O design ficou focado para a manufatura (DFM), permitindo que peças fossem apenas parafusadas/plugadas.

### 16 Fev 2026: Only added the hours of Flavortown
Atualização de acompanhamento das horas gastas no Hackatime. Neste ponto, grande parte do tempo foi dedicado a encontrar as dimensões exatas e refinar o CAD do gabinete para encaixar o hardware perfeitamente.

### 19 Fev 2026: Hardware Freeze & Modular Architecture
Depois de dezenas de horas ajustando posições e distâncias, cheguei ao "Hardware Freeze" da versão 1.0.

- Integrei o display OLED SPI (1.5" RGB).
- A bateria LiPo ganhou seu circuito definitivo de gestão.
- O maior estresse do dia foi preparar os arquivos para a fabricação na JLCPCB:
  1. Meu logo ("THE NERVE") estava sumindo do render 3D. Descobri que importei a imagem como "Documentação" no EasyEDA; converti o atributo para a camada `TopSilkLayer` para garantir que a JLCPCB imprimisse na placa.
  2. Ao subir os Gerbers, a JLCPCB cobrou **$80** para 5 placas. Fui revisar os logs de configuração e percebi que a opção "Epoxy Filled & Capped Vias" estava ativada. Desliguei isso, mudei pro acabamento HASL comum em placa branca e o custo caiu para a média esperada de **$10**.

### Próximos Passos (Pós-Freeze)
Com os Gerbers validados, o foco muda para a base do firmware:
1. Ambiente MicroPython no ESP32-S3.
2. Escrever drivers básicos do OLED.
3. Classe de inputs para o Joystick Hall e Encoder Óptico.

### 22 Fev 2026: Case Slim & Premium — O Enclosure Ficou do Jeito Certo

Depois do Hardware Freeze, eu achei que a parte mais difícil tinha acabado. Errei feio. 

Entrei no **OnShape** para modelar o enclosure e descobri que transformar uma tabela de dimensões em uma caixa 3D real é um desafio completamente diferente de projetar um circuito. A cada hora, alguma coisa que parecia resolvida no papel revelava um problema novo na modelagem. 

Passei cerca de **18 horas** trabalhando duro no CAD até a carcaça ficar com cara de produto de verdade: compacta, limpa e com um esquema de tampa inferior que dá total confiança pra montar, sem gambiarras.

**A Modelagem Completa da Case no OnShape**
A carcaça é um wedge trapezoidal com 15° de inclinação, paredes de 3mm e dimensões de 100x80mm na base. Cada furo foi posicionado com precisão:

- **OLED 1.5":** Janela de 40x40mm com chanfro de 45° para esconder as bordas do módulo.
- **Encoder Óptico:** Furo de 10mm com 25mm de folga livre pro knob girar.
- **Joystick Hall:** Furo de 25mm garantindo o tilt completo sem raspar.
- **Cherry MX (Execute):** Recorte cirúrgico de 14.05x14.05mm. Essa tolerância foi pensada pro switch entrar em *press-fit* perfeito, sem cola.
- **Missile Switch (Panic):** Furo M12 de 12.5mm e 50mm de vão livre para a capa vermelha abrir sem bater no joystick.
- **USB-C na frente:** Botei o conector pra sair onde realmente faz sentido pra placa e pro uso diário. Acabou o problema do pino ficar fundo demais ou num lugar ruim na mesa.
- **LED RGB cirúrgico:** Usei o centro do USB-C como referência e apliquei offset exato pra bater no furo de 5mm do light pipe.

**O grande pulo estrutural: Tampa Separada**
Antes, projetar tudo num sólido só ia dificultar demais o fatiamento e a manutenção. Dividi o código do OnShape em dois: a caixa principal e a tampa inferior (*flush-inside*). A tampa encaixa por dentro da base e trava nos 4 pilares internos. A placa fica presa direto nela, super pro.

LEMBRAR DE COLOCAR IMAGEM AQUI SOBRE o print/render do OnShape mostrando a vista isométrica da case inteira cortada, com os furos posicionados.

LEMBRAR DE COLOCAR IMAGEM AQUI SOBRE um close no OnShape focando no alinhamento cravado do LED RGB com o conector frontal.

LEMBRAR DE COLOCAR IMAGEM AQUI SOBRE o sistema de encaixe da tampa inferior com os pilares (Exploded View ou corte lateral).

**Sobre o Buzzer e a Térmica**
Decidi não furar a frente pro buzzer. Fiz 7 slots verticais (2x30mm) na parede traseira. Eles tiram o calor do ESP32-S3 (240MHz + Wi-Fi) e funcionam como grade acústica pro som sair limpo. A frente da case continua *stealth* e intacta.

LEMBRAR DE COLOCAR IMAGEM AQUI SOBRE os slots traseiros modelados no OnShape.

O próximo passo é rodar os testes de impressão pra confirmar a tolerância no mundo físico e preparar os arquivos CAD (.step/.stl) pra mandar pro Blueprint.

### 23 Fev 2026: Correção de BOM e Checkout na LCSC para PCBA
**(Hardware Fixes - Log V3)**

Achei que os arquivos Gerbers e o CAD estivessem prontos, mas na hora de fechar o pedido de montagem automática (PCBA) na LCSC/JLCPCB, tomei uma chuva de erros no sistema deles: `item does not found`, `shortfall` e `unmatched components`.

A causa foi que minha BOM original (feita para controle financeiro) tinha peças da Amazon e Mouser, e a máquina de Pick and Place da fábrica enlouqueceu tentando achar essas peças no catálogo deles.

**O que foi corrigido para a PCBA:**
1. **Limpeza da BOM e CPL:** Gereio um arquivo de 16 colunas exclusivo do EasyEDA, removendo todos os componentes mecânicos e externos (Cherry MX, Joystick Hall, ESP32-S3, OLED).
2. **Correção de Lotes (MOQ):** O Buzzer e o LED RGB genéricos estavam dando erro. Encontrei as peças exatas no catálogo deles (`QMB-09B-03` e `XL-A504RGBW`) e ajustei a matemática da BOM para refletir as quantidades mínimas de compra (bandeja de 5 buzzers e pacote de 10 LEDs).
3. **Substituição de Conectores THT:** Os conectores JST (Bateria) e PH (Expansão) estavam marcados como "Unmatched". Troquei pelo JST original `B2B-PH-K-S` e pelo Megastar `ZX-HY2.0-8PZZ` que tinham estoque na hora.
4. **Remoção do Decoder LS7183N-S:** A máquina acusou falta de estoque ("5 shortfall") para esse IC. Para não travar a produção inteira por causa de um chip, removi ele da montagem automática. Vou comprar separado e soldar em casa.

Os novos arquivos `BOM_JLCPCB_Final_V2.csv` e `CPL_JLCPCB_Final_V2.csv` passaram lisos no sistema deles. A placa base será montada na fábrica (SMD) e a "fun part" da montagem THT pesada vai sobrar pra mim.

**Status atual da Bill of Materials (Financeiro):**
O custo total do projeto foi atualizado para **$171.92**, refletindo as quantidades mínimas obrigatórias dos componentes da LCSC.
