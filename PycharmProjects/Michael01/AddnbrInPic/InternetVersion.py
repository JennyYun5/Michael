from PIL import Image, ImageDraw, ImageFont
import os
QQim = Image.open("Song.png")
w, h = QQim.size
font = ImageFont.truetype(os.path.join('fonts', 'simsun.ttc'), int(h / 4))
ImageDraw.Draw(QQim).pieslice([(w/3*2, 0),(w, h/3)] , 0, 360, fill='red')
ImageDraw.Draw(QQim).text((w*0.76, h*0.02), '1', font=font, fill='white')
QQim.show()
QQim.save("QQim.png")
