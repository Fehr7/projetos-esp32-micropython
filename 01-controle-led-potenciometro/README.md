# Controle de LED com Potenciômetro — ESP32

## Objetivo
Controlar o brilho de um LED usando um potenciômetro, com programação em MicroPython no ESP32.

## Componentes
- ESP32
- LED
- Resistor para o LED
- Potenciômetro
- Protoboard e jumpers

## Conexões
- LED: GPIO 12, com resistor em série.
- Potenciômetro: terminal central conectado ao GPIO 35.
- Terminais laterais: alimentação e GND, respeitando os limites elétricos do ESP32.

## Funcionamento
O ESP32 utiliza o ADC para ler a posição do potenciômetro. Essa leitura é convertida em um valor de PWM, que controla o brilho do LED.

Ao girar o potenciômetro, o brilho do LED muda de acordo com a leitura.

## Tecnologias
- MicroPython
- ESP32
- ADC
- PWM

## Aprendizados
Este projeto explora leitura analógica, controle PWM e interação entre software e componentes eletrônicos.

## 🎥 Demonstração do projeto

Confira o projeto funcionando na prática:

▶️ [https://youtu.be/X4lEmjtZeB0](https://youtu.be/X4lEmjtZeB0)

O vídeo demonstra o controle do brilho de um LED utilizando um potenciômetro, ESP32 e MicroPython.
