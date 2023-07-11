import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from time import sleep
from adafruit_epd.ssd1675 import Adafruit_SSD1675

from PIL import Image, ImageDraw, ImageFont
import socket

import sys

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None

display = Adafruit_SSD1675(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)

display.rotation = 1

display_text = ""

if len(sys.argv) > 1:
    display_text = str(sys.argv[1])
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    display_text = s.getsockname()[0]
    s.close()


image = Image.new("RGB", (display.width, display.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

FONTSIZE = 28
TEXT_COLOR = (0, 0, 0)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
BACKGROUND_COLOR = (0xFF, 0xFF, 0xFF)

draw.rectangle((0, 0, display.width - 1, display.height - 1), fill=BACKGROUND_COLOR)

# Draw Some Text
text = "Hello World!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (2, display.height // 2 - FONTSIZE),
    display_text,
    font=font,
    fill=TEXT_COLOR,
)

# Display image.
display.image(image)

display.display()



