# ImageFont
from PIL import ImageFont, ImageDraw, Image, ImageColor
import os
image = Image.open(os.path.join(os.path.dirname(__file__), 'Peng.jpg'))
draw = ImageDraw.Draw(image)
# font = ImageFont.load("arial.pil")
# draw.text((10,10), 'hello', font=font) # 图像image坐标(10,10)位置将出现“Hello”字样
font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simsun.ttc'), 150, index=0) # simsun.ttc是“宋体、新宋体、宋体-PUA”三种字体的集合, 但感觉只有两种吧， index != 2
a=draw.text((100,250), 'world', font=font) # 图像image坐标(100,250)位置将出现“world”字样
# image.show()
# PIL.ImageFont.ImageFont.getsize(text)
# PIL.ImageFont.ImageFont.getmask(text, mode='')

print(image.size) # (960, 1280)
draw.line((0,0)+image.size, fill=128) # \
draw.line((0,image.size[1], image.size[0], 0), fill=128)  # /
# image.show()

# print(ImageColor.getrgb("#ff0000")) # (255, 0, 0)  and rgb(255,0,0) / rgb(100%,0%,0%) / hsl(0,100%,50%) / "red" has same print
# print(ImageColor.getcolor("red", "P")) # (255, 0, 0) Mode need be RGB/p , otherwise will print 灰度值


print('-'*20 + 'PIL.ImageDraw.Draw'+'-'*20)
blank = Image.new('RGB', [960,1280], 'white')
    # drawObject.line([x1,y1,x2,y2] ,options) 以(x1,y1)为起始点，以(x2,y2)为终止点划一条直线。
drawObject = ImageDraw.Draw(blank)
# drawObject.line([100,100,100,600],fill = 'blue',width=20) # 左 |
# drawObject.line([(100,100),600,100],fill = 128,width=20) # 上—
# drawObject.line([(600,100),(600,600)],"black",width=20) # 右 |
# drawObject.line((100,600,600,600),fill = "yellow",width=20) # 下_
# blank.show()

    # drawObject.arc([x1, y1, x2, y2],  startAngle,  endAngle,  options)
# 在左上角坐标为(x1,y1)，右下角坐标为 (x2,y2)的矩形区域内满圆O内，以starangle为起始角度，
# endAngle为终止角度，截取圆O的一部分圆弧画出来
# [x1,y1,x2,y2]规定矩形框的水平中位线为0度角，角度顺时针变大（与数学坐标系规定方向相反！！）
# #画一个60度蓝色圆弧
# drawObject.arc((100,100,600,600),0,90,fill = "blue")
# #画一个上半圆弧
# drawObject.arc((100,100,600,600),180,360,fill = "red")
# #画一个右半椭圆，只需改区域大小为长方形
# drawObject.arc((100,100,600,400),90,270,fill = "yellow")
# blank.show()

    # drawObject.ellipse([x1,y1,x2,y2],  options)
# # 用法同arc，用于画圆（或者椭圆）， Options选项中fill表示将圆（或者椭圆）用指定颜色填满，outlie表示只规定圆的颜色
# drawObject.ellipse((100,100,600,600),outline = 128)
# drawObject.ellipse((100,250,600,450),fill = "blue")
# blank.show()

    # drawObject.chord([x1, y1, x2, y2],  startAngle,  endAngle,  options)
# 用法与arc相同，用来画圆从startAngle到endAngle的弦， Options选项中fill表示将弦与圆弧之间空间用指定颜色填满，outlie表示只规定弦线的颜色
#画圆
# drawObject.ellipse((100,100,600,600),outline = 128)
# #画一条弦
# drawObject.chord((100,100,600,600),0,90,outline = "red")
# #画弦并且将弦与弧包围区域涂色
# drawObject.chord((100,100,600,600),90,180,fill = "red")
# blank.show()

    #drawObject.pieslice([x1,y1,x2,y2],  startAngle,  endAngle,  options)
# 用法与ellipse相同，用于画起始角度间的扇形区域， options选项中fill选项将扇形区域用指定颜色填满，outline选项只用指定颜色描出区域轮廓，示例如下：
# #画一个圆
# drawObject.ellipse((100,100,600,600),outline = 128)
# #在上一行画出的园内画180度到210度的扇形区域轮廓
# drawObject.pieslice((100,100,600,600),180,210,outline = 128)
# #画60度到90度的扇形区域
# drawObject.pieslice((100,100,600,600),60,90,fill = "blue")
# blank.show()

    # drawObject.polygon(([x1,y1,x2,y2，…],options)
# 根据坐标画多边形，python会根据第一个参量中的xy坐标对，连接出整个图形
# options选项中fill选项将多边形区域用指定颜色填满，outline选项只用指定颜色描出区域轮廓，示例如下：
# drawObject.polygon([(200,200),(600,300),(300,600)],outline = "red")
# drawObject.polygon([(300,300),(500,300),(300,500),(500,500)],fill = "red")
# blank.show()

    # drawObeject.rectangle([x1,y1,x2,y2],options)
# 在给定区域内画一个矩形，(x1,y1)表示矩形左上角坐标值，(x2,y2)表示矩形右下角坐标值
# options选项中fill选项将多边形区域用指定颜色填满，outline选项只用指定颜色描出区域轮廓，示例如下：
# #画矩形
# drawObject.rectangle((200,200,500,500),outline = "red")
# drawObject.rectangle((250,300,450,400),fill = 128)
# blank.show()

    # drawObject.text(position,  string,  options)
# 在图像内添加文字
# Position是一个二元元组，指定字符串左上角坐标，string是要写入的字符串
# options选项可以为fill或者font(只能选择其中之一作为第三参量，不能两个同同时存在，要改变字体颜色，见ImageFont模块中的NOTE)。其中fill指定字的颜色，font指定字体与字的尺寸，font必须为ImageFont中指定的font类型，具体用法见ImageFont.Truetype()
# 第三参量为font示例参见下文ImageFont.Truetype()，第三那参量为fill时示例如下：
#在空白图像上矩形区域内添加文字
text = "I love python!"
drawObject.rectangle((200,200,500,500),outline = "red")
drawObject.text([300,350],text,"red")
blank.show()

    # drawObject.textsize(string,  options)
# 这个函数返回一个两元素的元组，是给定字符串像素意义上的size


