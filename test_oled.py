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
draw.text((10,10),'Hello JURA',  font=font, fill=255)
disp.image(image)
disp.display()
