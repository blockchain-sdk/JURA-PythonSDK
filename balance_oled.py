# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from api import sdk2
import Adafruit_SSD1306 as ssd1306
disp = ssd1306.SSD1306_128_32(rst=24,i2c_address=0x3C)
disp.begin()
disp.clear()
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
balance = sdk2.getbalance("R3UREqoYnn5eyoxuTSGqUCnxxoHCGN2N6X6dZv9qWbHSyd5DvBnH2abXESgLYbtWfzmVVncV9gg7s7tQoeMhy9qE")
draw.text((10,10),"{0}".format(balance),  font=font, fill=1)
disp.image(image)
disp.display()
