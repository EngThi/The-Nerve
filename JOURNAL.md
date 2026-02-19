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