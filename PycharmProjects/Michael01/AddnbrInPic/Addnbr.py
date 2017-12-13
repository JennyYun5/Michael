from PIL import Image, ImageFont, ImageDraw
import os

Nbr = Image.open("Nbr.png")  # (225, 219)

txtnbr = input("Please enter the number : ")
txt = Image.new("RGBA", Nbr.size, color=None) # this is backgroud color (255, 255, 255, 0) , if RGBA  then None mean no backgroud
nbr = ImageDraw.Draw(txt)
font = ImageFont.truetype(os.path.join('fonts', 'simsun.ttc'), 200) # 200 is font size
nbr.text((60, 15), txtnbr, font=font, fill="#000000") # is txt location
txt.save("AddUsernbr.png")
img1 = Nbr.convert('RGBA') #图片为RGBA
out_img = Image.alpha_composite(img1, txt)
out_img.save("outNbr.png")

Song = Image.open("Song.png")
Songnbr = out_img.resize((50, 50))
box = (0, 0, 50, 50)
region = Songnbr.crop(box)
Song.paste(region, box)
Song.save("Final.png")

