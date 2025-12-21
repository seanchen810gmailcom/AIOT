#########################匯入模組#########################
import time
import mcu
from machine import ADC, Pin, I2C
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
# mq_server = "192.168.68.114"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqtt = mcu.MQTT(mqttClientId, mq_server, mqtt_username, mqtt_password, keepalive=30)

mqtt.connect()

mqtt.subscribe("System", on_message)

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
LED.LED_open(0, 0, 0)
light_sensor = ADC(0)  # 建立 ADC 物件
m = ""
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#########################主程式#########################
while True:
    # 查看是否有訂閱主題發布的資料
    mqtt.check_msg()  # 等待已訂閱的主題發送資料

    light_sensor_reading = light_sensor.read()  # 讀取類比數位轉換器輸出
    長度 = len(m)
    oled.fill(0)  # 清除螢幕
    if m == "on":
        LED.LED_open(1, 1, 1)
        oled.text(m, 0, 0)  # 顯示文字,X座標, Y座標
    elif m == "off":
        LED.LED_open(0, 0, 0)
        oled.text(m, 0, 0)  # 顯示文字,X座標, Y座標
    elif m == "auto":
        oled.text(m, 0, 0)  # 顯示文字,X座標, Y座標
        if light_sensor_reading > 700:
            LED.LED_open(1, 1, 1)
        else:
            LED.LED_open(0, 0, 0)
    else:
        for i in range(0, 長度, 12):
            oled.text(m[i : i + 12], 0, (i // 12) * 10)  # 顯示文字,X座標, Y座標
    oled.show()
    time.sleep(0.1)
