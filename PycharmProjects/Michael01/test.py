from __future__ import print_function
from PIL import Image, ImageFilter, ImageSequence, TarIO, ImageEnhance

import os, sys

_im = "Song.jpg"


def ConvertToPng():
    f, e = os.path.splitext(_im)
    fout = f + ".png"
    if _im != fout:
        try:
            im.save(fout)
        except IOError:
            print("Can't convert!")


def CreateJPEGThumbnails(im):
    size = (128,128)
    fout = os.path.splitext(_im)[0] + '.thumbnail'
    if _im != fout:
        try:
            im.thumbnail(size)
            im.save(fout,'JPEG')
        except IOError:
            print("cannot create thumbnail for", im)


def CutPastMergeIm(im):
    box = (100, 165, 150, 200)
    region = im.crop(box)
    print(region.size)
    # region = region.transpose(Image.ROTATE_180)
    region.save("SongRegion.jpg")
    # im.paste(region, box)


def Rollimage(im, delta):
    "Rolling an image sideways"

    xsize, ysize = im.size
    delta = delta % xsize
    if delta == 0:
        return im
    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    part1.load()
    part2.load()
    im.paste(part2, (0, 0, xsize-delta, ysize))
    im.paste(part1, (xsize-delta, 0, xsize, ysize))
    return im


def SplitMergeimage(im):
    r, g, b = im.split()
    print(r, g, b)
    # if (r,g,b) same as before .  b(blure) g(green) r(red)
    im = Image.merge("RGB", (b, r, g))
    im.show()


def GeometryImage(im, angle):
    fout = im.resize((400, 400))
    # fout = fout.rotate(angle)
    fout = fout.transpose(Image.FLIP_LEFT_RIGHT)
    fout.show()
    fout = fout.transpose(Image.FLIP_TOP_BOTTOM)
    fout.show()
    fout = fout.transpose(Image.ROTATE_180)
    fout.show()


def ColorTrans(im):
    im = im.convert("L")
    im.show()


def ImageEnhance(im):
    f, e = os.path.splitext(_im)
    print(f, e)
    im.filter(ImageFilter.DETAIL).save(os.path.join("Filter", f) + "Detail.jpg")
    im.filter(ImageFilter.BLUR).save(os.path.join("Filter", f) + "Blur.jpg")
    im.filter(ImageFilter.CONTOUR).save(os.path.join("Filter", f) + "Contour.jpg")
    im.filter(ImageFilter.EDGE_ENHANCE).save(os.path.join("Filter", f) + "Edge.jpg")
    im.filter(ImageFilter.EMBOSS).save(os.path.join("Filter", f) + "Emboss.jpg")
    im.filter(ImageFilter.FIND_EDGES).save(os.path.join("Filter", f) + "Findedge.jpg")
    im.filter(ImageFilter.SMOOTH).save(os.path.join("Filter", f) + "Smooth.jpg")
    im.filter(ImageFilter.SHARPEN).save(os.path.join("Filter", f) + "Sharpen.jpg")
    im.filter(ImageFilter.GaussianBlur(radius=10)).save(os.path.join("Filter", f) + "Gauss.jpg")
    im.filter(ImageFilter.UnsharpMask(radius=3, percent=100, threshold=2)).save(os.path.join("Filter", f) + "Unsharp.jpg")

    fout1 = im.point(lambda x: x * 0.2)   # let image dark -> light
    source = im.split()  # default split R G B order
    R, G, B = 0, 1, 2
    mask = source[R].point(lambda x: x * 2)
    # mask.show()
    out = source[G].point(lambda x: x * 0.5)
    # out.show()
    source[G].paste(out, None, mask)
    im = Image.merge(im.mode, source)
    # im.show()
    # *******************************************************************
    # issue 1 :below code can not process
    # *******************************************************************
    # enh = ImageEnhance.Contrast(im)
    # enh.enhance(1.3).show("30% more contrast")

    ImageEnhance.Brightness(im).enhance(1.5).save(os.path.join("Enhance", f) + "Brightness.jpg")


def ImageSeq():
    Gifmulan = Image.open('Mulan.gif')
    # Gifmulan.seek(1)
    # try:
    #     while 1:
    #         Gifmulan.seek(Gifmulan.tell() + 1)
    # except EOFError:
    #     pass

    for frame in ImageSequence.Iterator(Gifmulan):
        pass
        # frame.show()


if __name__ == '__main__':
    im = Image.open(_im)  # print(im)  <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=240x240 at 0x27EFB30>
    print("original = ", im.format, im.size, im.mode)
    # im.show()
    # ConvertToPng()
    # CreateJPEGThumbnails(im)
    # CutPastMergeIm(im)
    # Rollimage(im, 100)
    # im.show()
    # SplitMergeimage(im)
    # GeometryImage(im, 45)
    # ColorTrans(im)
    ImageEnhance(im)
    # ImageSeq()   # show Mulan1.gif

    # *******************************************************************
    # issue 2 :below code can not process
    # *******************************************************************
    # fp = TarIO.TarIO("Pic.tar", "Wangzhe.jpg")
    # im01 = Image.open(fp)

    # im.draft("L", (100, 100))
    # print("draft = ", im.mode, im.size)
