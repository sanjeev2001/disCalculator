from mathpix.mathpix import MathPix
from PIL import Image
import requests
import wolfram
import wolframalpha
import time

reader = MathPix(
    app_id="discalculator_gmail_com_f307ad", app_key="684b628a6ac77aeb3d1f"
)
# ocr = reader.process_image(
#     image_url="https://cdn.discordapp.com/attachments/705540726963961867/706212921348194315/algebra.png"
# )

# preview(ocr.latex, filename="output.png")

# formula = ocr.latex.replace("\n", " ")
# r = requests.get(
#     "http://latex.codecogs.com/png.latex?\dpi{{300}} {formula}".format(formula=formula)
# )
# f = open("example.png", "wb")
# f.write(r.content)
# f.close()

# im = Image.open("example.png")
# rgb_im = im.convert("RGB")
# rgb_im.save("pls.jpg")
wolfclient = wolframalpha.Client("L766YW-6V34XVRVWG")

res = wolfclient.query("integrate e^x")
print((res.details).get("Indefinite integral"))

# res = wolfclient.query("derivative 3x^2")
# print((res.details).get("Derivative"))

# print(wolfram.query("derivative", "3 x ^ { 2 }"))
