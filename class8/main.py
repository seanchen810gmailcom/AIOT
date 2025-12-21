##################################匯入模組#################################################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC

#################################函式與類別定義#######################################
m = ""


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")
    m = msg


wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
# mq_server= "192.168.68.144"
mqttClientId = "Sean"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)
gpio = mcu.gpio()
RED = Pin(gpio.D5, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)

try:
    mqClient0.connect()
except:
    sys.sxit()
finally:
    print("connected MQTT server")

mqClient0.set_callback(on_message)  # 設定接受訊息的時候要呼叫的函式
mqClient0.subscribe("System")  # 設定想訂閱的主提
#################################主程式#########################################
while True:
    # 查看是否有訂閱主題發吧的資料
    mqClient0.check_msg()  # 等待已訂閱的主題發送資料
    mqClient0.ping()  # 持續確認是否還保持連線
    time.sleep(0.1)
    if m == "on":
        BLUE.value(1)
        RED.value(1)
        GREEN.value(1)
    elif m == "off":
        BLUE.value(0)
        RED.value(0)
        GREEN.value(0)
