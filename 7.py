import Image
import re
import urllib

urllib.urlretrieve ("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
from PIL import Image
im = Image.open('oxygen.png')
width = im.size[0]
height = im.size[2]
halfway_down = im.size[2]/2
block_size = 7
row = [im.getpixel((x, halfway_down)) for x in range(0, width, block_size)]
ords = [r for r, g, b, a in row if r == g == b]
message = "".join(map(chr, ords))
next_level_ords = re.findall('\d+', message)
"".join(map(chr, map(int, next_level_ords)))
