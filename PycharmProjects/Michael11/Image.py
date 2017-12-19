from PIL import Image, ImageFilter
import os

im = Image.open(os.path.join(os.path.dirname(__file__), 'Song.jpg'))
imSong = Image.open(os.path.join(os.path.dirname(__file__), 'Song.gif'))
print('-'*20+'Image 属性'+'-'*20)
#     # Format  源文件的文件格式。如果是由PIL创建的图像，则其文件格式为None。
# print(im.format) # JPEG
#     # Mode 图像的模式。这个字符串表明图像所使用像素格式。该属性典型的取值为“1”，“L”，“RGB”或“CMYK”
# print(im.mode) # RGB
#     # Size 图像的尺寸，按照像素数计算。它的返回值为宽度和高度的二元组（width, height）。
# print(im.size) # (960, 1280)
#     # Palette 颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。
# print(im.palette) # None
# print(imSong.palette) # <PIL.ImagePalette.ImagePalette object at 0x0223E630>
#     # Info 存储图像相关数据的字典
# print(im.info)
print('-'*20+'Image 方法'+'-'*20)
    # Convert 将当前图像转换为其他模式，并且返回新的图像
# print(im.mode)
# im01=im.convert('L')
# print(im01.mode)
    # im.convert(“P”,**options)  这个与第一个方法定义一样，但是当“RGB”图像转换为8位调色板图像时能更好的处理
    # Dither=. 控制颜色抖动。默认是FLOYDSTEINBERG，与邻近的像素一起承担错误。不使能该功能，则赋值为NONE。
    # Palette=. 控制调色板的产生。默认是WEB，这是标准的216色的“web palette”。要使用优化的调色板，则赋值为ADAPTIVE。
    # Colors=. 当选项palette为ADAPTIVE时，控制用于调色板的颜色数目。默认是最大值，即256种颜色。
    # im.convert(mode,matrix) 使用转换矩阵将一个“RGB”图像转换为“L”或者“RGB”图像。变量matrix为4或者16元组。
# rgb2xyz = (0.412453,0.357580, 0.180423, 0,
#            0.212671,0.715160, 0.072169, 0,
#            0.019334,0.119193, 0.950227, 0 )
# im02 = im.convert('L', rgb2xyz)
# im02.show()
    # im.copy() 拷贝这个图像。如果用户想粘贴一些数据到这张图，可以使用这个方法，但是原始图像不会受到影响。
# imcopy = im.copy()
# imcopy.show()
    # im.crop(box) 从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标。
# 这是一个懒操作。对源图像的改变可能或者可能不体现在裁减下来的图像中。为了获取一个分离的拷贝，对裁剪的拷贝调用方法load()。
# box = [0,0,150,150]
# im_crop = im.crop(box)
# im_crop.show()
    # im.draft(mode,size)配置图像文件加载器，使得返回一个与给定的模式和尺寸尽可能匹配的图像的版本。
    # 例如，用户可以使用这个方法，在加载一个彩色JPEG图像时将其转换为灰色图像，或者从一个PCD文件中提取一个128x192的版本。
    # 注意：这个方法会适时地修改图像对象（精确地说，它会重新配置文件的读取器）。如果图像已经被加载，那这个方法就没有作用了
# im.draft("L", (50,50))
# im.show()
    # im.filter(filter) 返回一个使用给定滤波器处理过的图像的拷贝
# im_filter=im.filter(ImageFilter.BLUR)
# im_filter.show()
    # im.fromstring(data) 与函数fromstring()一样，但是这个方法会将data加载到当前的图像中
    # im.getbands()⇒ tuple of strings 返回包括每个通道名称的元组。例如，对于RGB图像将返回（“R”，“G”，“B”）
# print(im.getbands()) # ('R', 'G', 'B')
    # im.getbbox() 计算图像非零区域的包围盒。这个包围盒是一个4元组，定义了左、上、右和下像素坐标。如果图像是空的，这个方法将返回空。
# print(im.getbbox()) # (0, 0, 240, 240)
    # im.getcolors() 返回一个（count，color）元组的无序list，其中count是对应颜色在图像中出现的次数。
    # 如果变量maxcolors的值被超过，该方法将停止计算并返回空。变量maxcolors默认值为256。为了保证用户可以获取图像中的所有颜色，you can pass in size[0]*size[1]（请确保有足够的内存做这件事）。
# ls=im.getcolors(256)
# print(str(len(ls)))       # issue here
    # im.getdata() 以包含像素值的sequence对象形式返回图像的内容。这个sequence对象是扁平的，以便第一行的值直接跟在第零行的值后面，等等。
# # 注意：这个方法返回的sequence对象是PIL内部数据类型，它只支持某些sequence操作，包括迭代和基础sequence访问。使用list(im.getdata())，将它转换为普通的sequence。
# Sequence对象的每一个元素对应一个像素点的R、G和B三个值
# seq = im.getdata()
# seq0 = list(seq)
# print([seq[i] for i in range(2)]) # [(235, 195, 159), (231, 191, 155)]
# print([seq0[i] for i in range(2)]) # [(235, 195, 159), (231, 191, 155)]
    # im.getextrema()返回一个2元组，包括该图像中的最小和最大值
# print(im.getextrema()) # ((0, 255), (0, 255), (0, 228)) 该方法返回了R/G/B三个通道的最小和最大值的2元组
    # im.getpixel(xy) 返回给定位置的像素值。如果图像为多通道，则返回一个元组
    # 注意：该方法执行比较慢；如果用户需要使用python处理图像中较大部分数据，可以使用像素访问对象（见load），或者方法getdata()。
# print(im.getpixel((4, 4))) # (202, 164, 119)
# r, g, b = im.split()
# print(r.getpixel((4,4))) # 202
    # im.histogram() 返回一个图像的直方图。这个直方图是关于像素数量的list，图像中的每个象素值对应一个成员。如果图像有多个通道，所有通道的直方图会连接起来（例如，“RGB”图像的直方图有768个值）。
    # 二值图像（模式为“1”）当作灰度图像（模式为“L”）处理。
# ls = im.histogram()
# print(str(len(ls))) # 768
# print(str(ls[0])) # 3
    # im.histogram(mask) 返回图像中模板图像非零地方的直方图。模板图像与处理图像的尺寸必须相同，并且要么是二值图像（模式为“1”），要么为灰度图像（模式为“L”）。
    # im.load()方法load()返回一个用于读取和修改像素的像素访问对象。这个访问对象像一个二维队列
# pix = im.load()
# print(pix[0, 0]) # (235, 195, 159)
    # im.paste(image,box) 将一张图粘贴到另一张图像上。变量box或者是一个给定左上角的2元组，或者是定义了左，上，右和下像素坐标的4元组，或者为空（与（0，0）一样）。如果给定4元组，被粘贴的图像的尺寸必须与区域尺寸一样。
    # 如果模式不匹配，被粘贴的图像将被转换为当前图像的模式
# box = [0,0,100,100]
# im_crop = im.crop(box)
# im.paste(im_crop,(50,50))
# im.show()
    # im.paste(colour,box) 它与定义1一样，但是它使用同一种颜色填充变量box对应的区域。对于单通道图像，变量colour为单个颜色值；对于多通道，则为一个元组。
# im.paste((0,256,0),(0,0,100,100))
# im.show() # 图像im的（0，0）位置将出现一个100x100的绿色方块。
# 对于多通道的图像，如果变量colour只给定一个数值，将只会应用于图像的第一个通道。如果是“RGB”模式的图像，将应用于红色通道。
    # im.paste(image,box, mask) 它使用变量mask对应的模板图像来填充所对应的区域
# box = [100,100,150,150]
# im_crop = im.crop(box)
# r,g,b = im_crop.split()
# im.paste(im_crop,(0,0,50,50),r)
# # im.paste((0,256,0),,(0,0,50,50),r)
# im.show()
    # im.point(table) 返回给定查找表对应的图像像素值的拷贝。变量table为图像的每个通道设置256个值。如果使用变量function，其对应函数应该有一个参数。这个函数将对每个像素值使用一次，结果表格将应用于图像的所有通道。
    # 如果图像的模式为“I（整数）”或者“F（浮点）”，用户必须使用function方式，function必须按照下面的格式：
    # argument * scale+ offset
# out = im.point(lambda i: i * 1.2 + 10)
# out.show()
    #zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
    # 然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
    # 利用*号操作符，可以将list unzip（解压）
# a =[1,2,3]
# b =[2,3,4]
# b =[4,5,6]
# c =[4,5,6,7,8]
# print([i for i in zip(a,b)]) # [(1, 4), (2, 5), (3, 6)]
# print([i for i in zip(a,c)]) # [(1, 4), (2, 5), (3, 6)]
# zipped = zip(a,b)
# print([i for i in zip(*zipped)]) # [(1, 2, 3), (4, 5, 6)]
    # im.point(table,mode) 它会为输出图像指定一个新的模式。这个方法可以一步将模式为“L”和“P”的图像转换为模式为“1”的图像。
# r,g,b = im.split()
# # im = r.point(lambda x:x*1.3+5, "1") # 图片全白
# im= r.point(lambda x:x*0, "1") # 图片全黑
# im.show()
    # im.putalpha(band)
    # im.putdata(data)从sequence对象中拷贝数据到当前图像，从图像的左上角（0，0）位置开始。变量scale和offset用来调整sequence中的值：
    #pixel = value *scale + offset 如果变量scale忽略，则默认为1.0。如果变量offset忽略，则默认为0.0。
# r,g,b=im.split()
# print(r.getpixel((0,0))) # 235
# print(r.getpixel((0,1))) # 198
# r.putdata([1,2,3])
# print(r.getpixel((0,0))) # 1
# print(r.getpixel((0,1))) # 198
    # im.putpalette(sequence) 为“P”或者“L”图像增加一个调色板。对于“L”图像，它的模式将变化为“P”。调色板序列需要包含768项整数，每组三个值表示对应像素的红，绿和蓝。用户可以使用768个byte的字符串代替这个整数序列。
# >> > im01 = Image.open("D:\\Code\\Python\\test\\img\\test01.jpg")
# >> > r, g, b = im01.split()
# >> > r.mode
# 'L'
# >> > r.putpalette([1, 2, 3])
# >> > r.mode
# 'P'
    # im.resize(size) / im.resize(size, filter) 返回改变尺寸的图像的拷贝。变量size是所要求的尺寸，是一个二元组：（width, height）。
    # 变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一。如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST。
    # 在当前的版本中bilinear和bicubic滤波器不能很好地适应大比例的下采样（例如生成缩略图）。用户需要使用ANTIALIAS，除非速度比质量更重要。
# print(im.size)
# im = im.resize((50,50))
# print(im.size)
# im.show()
    # im.rotate(angle,filter=NEAREST, expand=0)  返回一个按照给定角度顺时钟围绕图像中心旋转后的图像拷贝。
    # 变量filter应该是NEAREST、BILINEAR或者BICUBIC之一。如果省略该变量，或者图像模式为“1”或者“P”，则默认为NEAREST。
    # 变量expand，如果为true，表示输出图像足够大，可以装载旋转后的图像。如果为false或者缺省，则输出图像与输入图像尺寸一样大。
# im01 = im.rotate(30)
# im01.show()
    # im.save(outfile, format, options…)
# im01.save("D:\Python\PycharmProjects\Michael11\save.jpg")
    # im.seek(frame)在给定的文件序列中查找指定的帧。如果查找超越了序列的末尾，则产生一个EOFError异常。当文件序列被打开时，PIL库自动指定到第0帧上。
# imSong.seek(8)
# imSong.show()
    # im.tell() 返回当前帧所处位置，从0开始计算。
# imSong.seek(8)
# print(imSong.tell())  # 8
    # im.thumbnail(size)
# im01.thumbnail((100,100))
    # im.transform(size,method, data)
# 使用给定的尺寸生成一张新的图像，与原图有相同的模式，使用给定的转换方式将原图数据拷贝到新的图像中。
# 在当前的PIL版本中，参数method为EXTENT（裁剪出一个矩形区域），AFFINE（仿射变换），QUAD（将正方形转换为矩形），MESH（一个操作映射多个正方形）或者PERSPECTIVE。
print(im.size)
tran = im.transform((50,50),Image.EXTENT,(0,0,200,200))
print(tran.size)
tran.show()
