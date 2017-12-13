from PIL import ImageDraw, Image

im = Image.open("Song.png")
draw = ImageDraw.Draw(im)

draw.line((0,0)+im.size,fill="black")
draw.line((0,im.size[1],im.size[0],0),fill="black")
im.show()

draw.arc((0,0,20,20),0,90,fill="black")
draw.arc((30,30,100,100),0,-90,fill="red")
draw.arc((100,100,200,200),-90,0,fill="green")
im.show()

im02 = Image.open("SongRegion.jpg")
r,g,b = im02.split()
draw.bitmap((0,0), r, fill="red")
im.show()


draw.chord((0,0,100,100), 0,90,fill="blue")
im.show()


draw.ellipse((100,100,150,150), fill="purple")
im.show()

