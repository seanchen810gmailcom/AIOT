#########################匯入模組#########################
from machine import Pin, ADC
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()
    print(f"value={light_sensor_reading},{round(light_sensor_reading*100/1024)}%")
    sleep(1)
    if light_sensor_reading > 700:
        print("好暗喔！\n我需要光！")
        BLUE.value(1)
        RED.value(1)
        GREEN.value(1)
    elif light_sensor_reading < 50:
        print("Ouch！太亮了!\n你好壞!\n不要傷害我!")
    else:
        BLUE.value(0)
        RED.value(0)
        GREEN.value(0)
