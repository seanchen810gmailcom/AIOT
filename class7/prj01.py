###########################################匯入模組#################################################
import paho.mqtt.client as mqtt
import pyttsx3


###########################################函式與類別定義############################################
def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"連線結果{reason_code}")
    client.subscribe("系統")


def on_message(client, userdata, msg):
    print(f"我訂閱的主題是：{msg.topic},收到訊息：{msg.payload.decode("utf-8")}")
    a = pyttsx3.init()
    a.say(f"我訂閱的主題是：{msg.topic},收到訊息：{msg.payload.decode("utf-8")}")
    a.runAndWait()


# 建立客戶端實例
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
# 設定連接成功後的回條函數
client.on_connect = on_connect
# 設定接收訊息後的回調函數
client.on_message = on_message
# 設定使用者名稱和密碼
client.username_pw_set("singular", "Singular#1234")
# 連接伺服器
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
# 保持連線
client.loop_forever()
