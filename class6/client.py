# PC執行
#############################匯入模組##################################
import socket
import pyttsx3
import time

#############################宣告與設定############################
client_socket = socket.socket()
client_socket.connect(("localhost", 3456))
pyttsx3 = pyttsx3.init()
#################################主程式##################################
while True:
    msg = input("Input Message:")  # 輸入想要傳送到伺服器的訊息
    client_socket.send(msg.encode("utf8"))  # 將訊息轉換為位元組後傳送到伺服器
    reply = client_socket.recv(128).decode("utf8")  # 將接受伺服器回傳的訊息並解碼
    if (
        reply
        == "System error!!! System offline!!! Explosion imminent, danger!!! BOON!!!!!!!!!"
    ):
        print("BOON!!!!!!!!!!")
        print(reply)
        pyttsx3.say(reply)
        pyttsx3.runAndWait()
        time.sleep(5)
        break
    print(reply)
    pyttsx3.say(reply)
    pyttsx3.runAndWait()

client_socket.close()
