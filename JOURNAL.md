# Diário de Desenvolvimento (Journal) - The Nerve

Este documento registra a evolução, as decisões de engenharia e os desafios enfrentados durante o desenvolvimento do **The Nerve V1**.

---

### Fase 1: Do Pânico à Resiliência (O Início)
O projeto começou como uma tentativa de criar uma interface física para automatizar fluxos de vídeo no `n8n`. Inicialmente, enfrentei um momento de "pânico" com a estrutura do projeto e ferramentas, o que me fez recomeçar o design do zero. Isso acabou sendo crucial: percebi que precisava de um controlador muito mais robusto do que um simples "teclado de macros".

### Fase 2: Pivot de Hardware (RP2040 vs. ESP32-S3)
A escolha do microcontrolador foi o primeiro grande divisor de águas.
- **Plano original:** RP2040. Era barato e eu já conhecia. Mas a falta de Wi-Fi/Bluetooth nativo limitaria o escopo para apenas automações locais via cabo.
- **A Decisão:** Migrei para o **ESP32-S3 ProS3[D]** da Unexpected Maker. Além do suporte nativo a USB HID (essencial para simular mouse/teclado), os 16MB de Flash e o Wi-Fi embutido abriram portas para enviar webhooks HTTP diretamente para meu servidor n8n sem depender do PC hospedeiro.

### Fase 3: A Transição para a Arquitetura Modular
Este foi o momento em que o "The Nerve" deixou de ser um brinquedo e virou uma ferramenta industrial.
- **O Problema:** Soldar componentes diretamente na placa (joystick, encoder, chaves) significa que se um quebrar, a placa inteira vai para o lixo. 
- **A Solução (DFM - Design for Manufacturing):** Decidi que **nada de interface seria soldado diretamente**. Implementei conectores universais usando terminais de parafuso e conectores JST (espaçamento de 2.54mm e 1.25mm). 
- **O Desafio do Roteamento:** Criar interfaces de 6 pinos que pudessem suportar módulos de 3.3V e 5V simultaneamente exigiu refazer todo o roteamento lógico da placa no EasyEDA. O layout ficou mais complexo, mas muito mais versátil.

### Fase 4: O "Hardware Freeze"
Depois de dezenas de horas ajustando posições e distâncias no EasyEDA, cheguei à versão final da PCB V1.0.
- Integrei o suporte para um **Display OLED SPI (1.5" RGB)** para feedback em tempo real.
- Adicionei gerenciamento de energia para bateria LiPo, tornando o cyberdeck portátil.
- O formato final foi validado para caber no gabinete trapezoidal (que deu bastante dor de cabeça no CAD - Onshape/OpenSCAD).

### Fase 5: Preparação para Fabricação (A Luta com a JLCPCB)
Gerar os arquivos para a fábrica quase custou o orçamento do projeto.
- **O Erro do Silkscreen:** Meu logo ("THE NERVE") foi importado incorretamente no EasyEDA como uma imagem de "Documentação". No render 3D ele simplesmente sumia. Tive que converter o atributo para a camada `TopSilkLayer` para garantir que a JLCPCB imprimisse na placa.
- **O Susto dos $80:** Ao fazer o upload dos arquivos Gerber na JLCPCB, o orçamento bateu inacreditáveis $80 para 5 placas simples de 2 camadas. 
- **A Solução Econômica:** Analisando os logs, percebi que havia ativado acidentalmente processos caríssimos (`Epoxy Filled & Capped Vias` e `ENIG`). Desativei esses processos de luxo (desnecessários para este projeto), mantive o acabamento padrão HASL (Lead-Free), escolhi a placa branca com serigrafia preta (padrão sem custo extra de impressão multicolorida) e **o preço caiu para justos $10**. 

### Próximos Passos
Com o hardware congelado e os Gerbers enviados para produção, o foco total agora se volta para a arquitetura de software:
1. Estabelecer o ambiente MicroPython.
2. Escrever os drivers do OLED SPI.
3. Criar a classe principal de `InputHandler` para mapear o Encoder Óptico e o Joystick de Efeito Hall.