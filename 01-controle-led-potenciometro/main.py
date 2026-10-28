import machine
import time

# --- Configuração do LED com PWM ---
pin_led = machine.Pin(2)
led_pwm = machine.PWM(pin_led)
led_pwm.freq(1000)

# --- Configuração do Potenciômetro com ADC ---
# O potenciômetro está conectado ao pino 34 (um pino que é apenas entrada ADC)
pot_pin = machine.Pin(34)
# Configura o ADC com 12 bits de resolução (0-4095) e atenuação máxima
# A atenuação permite que o pino leia a faixa completa de tensão (0-3.3V)
adc = machine.ADC(pot_pin)
adc.atten(machine.ADC.ATTN_11DB)

print("Gire o potenciômetro para controlar o brilho do LED.")

while True:
    # 1. Lê o valor do potenciômetro (0 a 4095)
    pot_valor = adc.read()

    # 2. Mapeia o valor para a escala do PWM (0 a 1023)
    # Como 4095 / 4 = 1023.75, podemos simplesmente dividir por 4.
    # Usamos a divisão inteira (//) para garantir um número sem casas decimais.
    duty_cycle_valor = pot_valor // 4

    # 3. Define o duty cycle do LED
    led_pwm.duty(duty_cycle_valor)

    # Pequena pausa para não sobrecarregar o processador
    time.sleep_ms(50)
