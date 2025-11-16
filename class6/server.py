# PC執行
################################匯入模組###################################
import socket
import time

###############################宣告與設定##################################
HOST = "localhost"  # IP
PORT = 3456  # Port, 可自行更改但需與客戶端相同
server_socket = socket.socket()  # 建立socket
server_socket.bind((HOST, PORT))  # 綁定IP和Port
server_socket.listen(5)  # 最大連街數量，超過則拒絕連接
print(f"surver:{HOST} port:{PORT} start")  # 顯示伺服器IP和PORT
client, addr = server_socket.accept()  # 接受客戶端連接，返回刻畫端socket和地址
print(f"client address:{addr[0]}port:{addr[1]}connected")  # 顯示客戶端IP和PORT

####################################主程式###################################
while True:
    msg = client.recv(512).decode("utf8")
    # 接受客戶端訊息，100為接受訊息的最大長度，utf8為解碼方式
    print(f"Receive Message:{msg}")  # 顯示接受到的訊息
    reply = ""  # 建立伺服器回應字串

    if msg == "Hi":
        reply = "Hello!"  # 將字串轉換為位元組，因為sockey只能傳送位元組
        client.send(reply.encode("utf8"))  # 這跟 client.send(b"Hello")是一樣的
    elif msg == "Bye":
        client.send(
            b"System error!!! System offline!!! Explosion imminent, danger!!! BOOOOOOOOON!!!!!!!!!"
        )
        time.sleep(6)
        break
    else:
        reply = "What??"
        client.send(reply.encode("utf8"))
client.close()  # 關閉與客戶端溝通
server_socket.close()  # 關閉伺服器
