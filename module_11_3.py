import pandas as pd
from PIL import Image, ImageFilter

csvframe1 = pd.read_csv('csv1.csv', header = None)
print(csvframe1)

csvframe2 = pd.read_csv('txt1.txt')
print(csvframe2)

csvframe2.to_csv('csv2.csv')

xlsframe = pd.read_excel('proof.xlsx')
print(xlsframe)

try:
    original = Image.open("double.jpg")
except FileNotFoundError:
    print("Файл не найден")

print("Размер изображения:")
print(original.format, original.size, original.mode)

# размываем изображение
blurred = original.filter(ImageFilter.BLUR)
# открываем оригинал и размытое изображение
original.show()
blurred.show()
# сохраняем изображение
blurred.save("blurred.png")

# эффект Контур
contoured = original.filter(ImageFilter.CONTOUR)
# открываем Контур
contoured.show()
# сохраняем изображение
contoured.save("contoured.jpg")

# эффект Мини
contoured = original.filter(ImageFilter.CONTOUR)
# открываем Контур
contoured.show()
# сохраняем изображение
contoured.save("contoured.jpg")

size = (128, 128)
saved = "mini.jpeg"
#img = Image.open("Lenna.png")
original.thumbnail(size)
original.save(saved)
original.show()