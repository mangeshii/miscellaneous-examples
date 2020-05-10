from PIL import Image
colorImage = Image.open("./eifel.jpeg")

rotated = colorImage.rotate(260)

rotated.show()

