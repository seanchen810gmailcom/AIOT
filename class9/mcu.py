# mcu.py
import sys
import network
from machine import PWM, Pin
from umqtt.simple import MQTTClient


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    """
    WIFI 類別用於管理 WIFI 連線。

    屬性:
        sta (WLAN): WIFI 模組。
        ap (WLAN): WIFI 模組。
        ssid (str): WIFI 名稱。
        password (str): WIFI 密碼。
        ap_active (bool): 是否開啟 AP 模式。
        sta_active (bool): 是否開啟 STA 模式。
        ip (str): WIFI 的 IP 位址。

    方法:
        setup(ap_active, sta_active): 設定 WIFI 模組。
        scan(): 搜尋 WIFI。
        connect(ssid, password): 連接 WIFI。
    """

    def __init__(self, ssid=None, password=None):
        """
        初始化 WIFI 模組
        ssid: WIFI 名稱
        password: WIFI 密碼

        使用方法：
        wi = wifi("WIFI_NAME", "WIFI_PASSWORD")
        """
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        """
        設定 WIFI 模組
        ap_active: 是否開啟 AP 模式
        sta_active: 是否開啟 STA 模式

        使用方法：
        wi.setup(ap_active=True|False, sta_active=True|False)
        """
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        """
        搜尋 WIFI
        返回: WIFI 列表

        使用方法：
        wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result:")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("STA 模式未啟用")

    def connect(self, ssid=None, password=None) -> bool:
        """
        連接 WIFI
        ssid: WIFI 名稱
        password: WIFI 密碼

        使用方法：
        wi.connect("WIFI_NAME", "WIFI_PASSWORD")
        或在初始化時有設定過就可以不用再設定
        wi.connect()
        """
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("STA 模式未啟用")
            return False

        if ssid is None or password is None:
            print("WIFI 名稱或密碼未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not (self.sta.isconnected()):
                pass
            self.ip = self.sta.ifconfig()[0]  # 取得 IP
            print("connet successfully", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        """
        LED 類別用於管理 RGB LED。

        屬性:
            RED (Pin): 紅色 LED。
            GREEN (Pin): 綠色 LED。
            BLUE (Pin): 藍色 LED。

        方法:
            __init__(r_pin, g_pin, b_pin, pwm=False): 初始化 LED。
                當 pwm=False 時，使用 Pin 控制 LED。
                當 pwm=True 時，使用 PWM 控制 LED。
        """
        self.pwm = pwm
        if pwm == False:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)
        else:
            frequency = 1000
            duty_cycle = 0
            self.RED = PWM(Pin(r_pin), freq=frequency, duty=duty_cycle)
            self.GREEN = PWM(Pin(g_pin), freq=frequency, duty=duty_cycle)
            self.BLUE = PWM(Pin(b_pin), freq=frequency, duty=duty_cycle)

    def LED_open(self, RED_value, GREEN_value, BLUE_value):
        """
        設定 LED 顏色亮度
            RED_value: 紅色亮度 (0-1023)
            GREEN_value: 綠色亮度 (0-1023)
            BLUE_value: 藍色亮度 (0-1023)

        使用方法：
            LED.LED_open(RED_value, GREEN_value, BLUE_value)

        例如：
            當 pwm=True 時，LED.LED_open(512, 0, 0) 代表紅色 LED 亮度為一半，綠色和藍色 LED 關閉
            當 pwm=False 時，LED.LED_open(1, 0, 0) 代表紅色 LED 開啟，綠色和藍色 LED 關閉
        """
        if self.pwm:
            self.RED.duty(RED_value)
            self.GREEN.duty(GREEN_value)
            self.BLUE.duty(BLUE_value)
        else:
            self.RED.value(RED_value)
            self.GREEN.value(GREEN_value)
            self.BLUE.value(BLUE_value)
