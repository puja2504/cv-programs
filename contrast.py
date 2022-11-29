from PIL import Image,ImageEnhance
img=Image.open("flower.jpg")
img.show()
enhancer=ImageEnhance.Contrast(img)
f=0.4
img_output=enhancer.enhance(f)
img_output.show()
f=4
img_output=enhancer.enhance(f)
img_output.show()
