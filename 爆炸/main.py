# PC執行
#############################匯入模組##################################
import socket
import time

#############################宣告與設定############################
client_socket = socket.socket()
client_socket.connect(("localhost", 3456))
#################################主程式##################################
while True:
    msg = "hello"  # 輸入想要傳送到伺服器的訊息
    client_socket.send(msg.encode("utf8"))  # 將訊息轉換為位元組後傳送到伺服器
client_socket.close()
