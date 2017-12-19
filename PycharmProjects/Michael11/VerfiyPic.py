from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random,string, os
list = []
[list.append(random.choice(string.ascii_letters)) for a in range(4)]

font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simsun.ttc'), 30, index=1)
img = Image.new('RGB', [300,100], 'white')
for x in range(0, img.width):
    for y in range(0, img.height):
        img.putpixel((x,y),(random.randint(100,200),random.randint(100,200),random.randint(100,200)))
draw = ImageDraw.Draw(img)
for i in range(4):
    draw.text((30+70*i, 30), str(list[i]), font=font, fill=(random.randint(0,50),random.randint(1,100),random.randint(200,255)))
img.filter(ImageFilter.BLUR)
img.save(r'D:\Python\PycharmProjects\Michael11\Random_code.jpg')

