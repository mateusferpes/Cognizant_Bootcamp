from PIL import Image


def convert(image):
    img = Image.open(image)
    imgGray = img.convert('L')
    imgGray.save(f'{image}_gray.jpg')

