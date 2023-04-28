from PIL import Image,ImageFilter
import os


def p3():

    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"
    f = "5.jpg"

    h = [a, b, c, d, f]
    for file in h:

        img = Image.open(file)
        new_img = img.filter(ImageFilter.SHARPEN)
        new_img.show()
        try:
            os.mkdir("D:/lera")
        except:
            pass
        new_img.save("D:/lera/new_img.png")


def p4():

    a = "1.jpg"
    b = "2.tiff"
    c = "3.jpg"

    h = [a, b, c]
    for file in h:
        if file.endswith('.jpg') or file.endswith('.png'):
            img = Image.open(file)
            newimg = img.filter(ImageFilter.SHARPEN)
            newimg.show()
            try:
                os.mkdir("D:/lera")
            except:
                pass
            newimg.save("D:/lera/newimg.png")

def p5():
    total = 0
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        print("Нужно купить:")
        for line in lines[1:]:
            product, quantity, price = line.strip().split(',')
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая сумма: {total} руб.")

p3(), p4(), p5()