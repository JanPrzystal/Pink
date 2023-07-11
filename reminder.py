import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from time import sleep
from adafruit_epd.ssd1675 import Adafruit_SSD1675

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None

up_button = digitalio.DigitalInOut(board.D5)
up_button.switch_to_input()
down_button = digitalio.DigitalInOut(board.D6)
down_button.switch_to_input()

display = Adafruit_SSD1675(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)

# flags that signify if action was completed
up_pressed = False
down_pressed = False

display.rotation = 1

# clear display and write example
display.fill(Adafruit_EPD.WHITE)

display.rect(0, 40, 20, 20, Adafruit_EPD.BLACK)
display.rect(0, 0, 20, 20, Adafruit_EPD.BLACK)

display.text("Euthyrox", 30, 4, Adafruit_EPD.BLACK)
display.text("Deuloxitine", 30, 44, Adafruit_EPD.BLACK)

display.display()

while not (up_pressed and down_pressed):
    sleep(0.1)
    if not (down_button.value or down_pressed):
        print("up pressed")
        display.line(2, 2, 18, 18, Adafruit_EPD.BLACK)
        display.line(2, 18, 18, 2, Adafruit_EPD.BLACK)
        display.display()
        down_pressed = True
    if not (up_button.value or up_pressed):
        print("down pressed")
        display.line(2, 42, 18, 58, Adafruit_EPD.BLACK)
        display.line(2, 58, 18, 42, Adafruit_EPD.BLACK)
        display.display()
        up_pressed = True





