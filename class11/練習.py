###############################匯入模組###############################
import mcu
from machine import Pin, I2C
import ssd1306

###############################宣告與設定###############################
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
###############################主程式###############################
oled.fill(0)  # 清除螢幕
oled.text("System Error", 0, 0)  # 顯示文字,X座標, Y座標
oled.text("About To Blow up", 0, 20)
oled.show()
