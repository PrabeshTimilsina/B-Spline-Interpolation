from PIL import Image

def grayScaleimage(img):
    grayscaleimg= img.convert("L")
    return grayscaleimg

