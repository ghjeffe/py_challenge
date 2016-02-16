from PIL import Image
import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
req = requests.get(url)
with open('oxygen.png', mode='wb') as fh:
    for chunk in req.iter_content(64):
        fh.write(chunk)
        
image1 = Image.open('oxygen.png')

# the grey boxes appear in rows 43 - 51 and are 7x9 (wxh) each
# it doesn't matter which row (43-51) you choose the result will be the same
row_pixels = [image1.getpixel((i, 45))[0] for i in range(0, image1.size[0], 7)]
text = ''.join(chr(int(num)) for num in row_pixels)
ords = re.findall('\d+', text)
print(''.join(chr(int(num)) for num in ords))

