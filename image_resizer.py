from PIL import Image

def resize_image(size1,size2):
    x = input("ENTER THE PHOTO NAME THAT YOU WANT TO RESIZE(in format xxxxxx.png/jpeg/jpg etc.):  ")
    image = Image.open(x)
    print(f"Current size : {image.size}")
    resize_image = image.resize((size1,size2))
    resize_image.save(x + str(size1) + "x" + str(size2) + "ENTER HERE A EXTENSION")   

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Lenght: "))
resize_image(size1,size2)

