
from machine import Pin, ADC, PWM
import time

# Configuração do LED com PWM
led = PWM(Pin(12))
led.freq(1000)

# Configuração do potenciômetro com ADC
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

print("Gire o potenciômetro para controlar o brilho do LED.")

while True:
    valor_pot = pot.read()

    # Converte a leitura do ADC (0 a 4095)
    # para o duty cycle do PWM (0 a 1023)
    brilho = valor_pot // 4

    led.duty(brilho)

    print("Leitura:", valor_pot, "| Brilho:", brilho)

    time.sleep(0.1)
