# 图像
#   用RGBA值来表示颜色（其中A表示透明度，0表示完全透明，255表示完全不透明）
#   white: (255, 255, 255, 255); red: (255, 0, 0, 255); green: (0, 255, 0, 255)
#   blue: (0, 0, 255, 255); gray: (128, 128, 128, 255); yellow: (255, 255, 0, 255)

# 处理电子表格Excel：
#   工具：openpyxl，LibreOffice Calc，OpenOffice Calc

# 处理文本文档Word：
#   工具：python-docx, LibreOffice Writer, OpenOffice Writer

# 处理PDF文档：





from PIL import Image, ImageFilter

def thumbnail_image():
    image = Image.open("C:/Users/Administrator/Pictures/代码.jpg")
    image.thumbnail((128, 128))
    image.show()

def Zoom_and_paste():
    image_1 = Image.open("C:/Users/Administrator/Pictures/代码.jpg")
    image_2 = Image.open("C:/Users/Administrator/Pictures/QQ图片.jpg")
    sub_image_1 = image_1.crop((12, 12, 89, 89))
    w, h = sub_image_1.size
    image_2.paste(sub_image_1.resize((int(w/0.8), int(h/0.8))), (189, 45))
    image_2.show()

def pixel_operating():
    image = Image.open("C:/Users/Administrator/Pictures/代码.jpg")
    for x in range(68, 128):
        for y in range(68, 128):
            image.putpixel((x, y), (0, 255, 0))
    image.show()

def Filter_Image():
    image = Image.open("C:/Users/Administrator/Pictures/代码.jpg")
    image.filter(ImageFilter.EDGE_ENHANCE).show()


if __name__=='__main__':
    # thumbnail_image()
    # Zoom_and_paste()
    # pixel_operating()
    Filter_Image()