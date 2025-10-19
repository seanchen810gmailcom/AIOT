#########################匯入模組#########################
import network

wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
# 搜尋wifi
wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])
Wlssid = "Singular_AI"
wipwd = "Singular#1234"
wlan.connect(Wlssid, wipwd)
while not wlan.isconnected():
    pass
print("coneted success", wlan.ifconfig())
while True:
    pass
#########################宣告與設定#########################

#########################主程式#########################
