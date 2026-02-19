![The Nerve PCB](assets/renders/Frontal_View.png)

# 🧠 The Nerve – Painel de Entrada Modular
![The Nerve Project Render](assets/renders/the_nerve_render_v2.png)

> **Status do Projeto:** Hardware Congelado / Desenvolvimento de Firmware (ESP32-S3)

**The Nerve** é um centro de comando tátil criado para trazer o controle físico de volta aos fluxos de trabalho digitais. Projetado inicialmente para automatizar pipelines de produção de vídeo (n8n + FFmpeg), sua arquitetura de hardware aberta o torna um controlador universal poderoso para desenvolvedores, editores e criadores.

Ele preenche a lacuna entre um teclado macro e uma interface cyberdeck totalmente programável.

## 🧱 A stack do Hardware
Construído em torno do **ESP32-S3 ProS3[D]** para recursos nativos de USB, Wi-Fi e Bluetooth.

- **Núcleo:** Unexpected Maker ESP32-S3 ProS3[D] (Dual-core 240MHz, 16MB Flash).

- **Feedback Visual:**
- **OLED:** Waveshare 1.5" RGB SPI (128x128) para status em tempo real, menus e dados da API.
- **LED RGB:** Indicações visuais imediatas (ex.: status do servidor, gravação ativa).

- **Encoder Óptico:** Rolagem/deslizamento de alta precisão.

- **Joystick de Efeito Hall:** Controle analógico sem deriva (parâmetros do mouse/XY).

- **Switches Mecânicos:** Cherry MX Green (Clicky) para uma execução satisfatória.

- **Interruptor de Míssil:** Interruptor com proteção de segurança para ações críticas (Implantar/Renderizar).
- **Feedback:** Buzzer passivo para alertas sonoros.

## 🔌 Arquitetura Modular
A placa de circuito impresso possui **terminais de parafuso e conectores JST**, permitindo a troca de sensores e entradas sem a necessidade de dessoldar.
- **Universal Interfaces de 6 pinos:** Suporta periféricos de 3,3 V e 5 V.
- **Preparado para bateria:** Gerenciamento integrado de LiPo para operação sem fio.

## 🚀 Aplicações potenciais
Além da automação de vídeo, o hardware é capaz de:
- **Controlador HID universal:** Teclado/Mouse/Dispositivo MIDI personalizado via USB-C.

- **Painel de controle IoT:** Monitore servidores, pipelines CI/CD ou Home Assistant via Wi-Fi/MQTT.

- **Ferramenta de desenvolvimento:** Botão físico "Implantar" com display de status para verificações de integridade da API.

- **Interface de acessibilidade:** Mapeamento de entrada personalizado para controle de software especializado.

## 📂 Estrutura do projeto

```text

├── BOM.csv <-- Lista oficial de materiais (LCSC + módulos externos)
├── README.md <-- Documentação do sistema
│
├── hardware/
│ ├── schematics/ # Arquivos de projeto EasyEDA
│ ├── pcb/ # Layout e roteamento da placa
│ ├── fabrication/ # Arquivos Gerber (prontos para JLCPCB)
│ └── 3d_models/ # Conceito de gabinete (arquivos STEP)
│
├── firmware/ # Lógica ESP32 (MicroPython ou Rust)
│ ├── src/ # Manipulação de entrada e drivers de display
│ └── lib/ # Bibliotecas de sensores
│
└── automation/ # Integração com o host (opcional)

├── n8n/ # Webhooks de exemplo de fluxo de trabalho
└── scripts/ # Listeners HID em Python
```

## Manufacturing Preview
![JLCPCB Checkout](hardware/fabrication/JLCPCB_Checkout.png)

_Projetado para quem precisa de mais do que apenas um atalho de teclado_
