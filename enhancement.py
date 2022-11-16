from PIL import Image
from PIL import ImageEnhance
i=Image.open("flower.jpg")
i.show()
new_bri=1.68
i_ori=ImageEnhance.Brightness(i)
i_bri=i_ori.enhance(new_bri)
i_bri.show()
cur_col=ImageEnhance.Color(i)
new_col=2.45
i_col=cur_col.enhance(new_col)
i_col.show()
cur_con=ImageEnhance.Contrast(i)
new_con=1.25
i_con=cur_col.enhance(new_con)
i_con.show()
cur_sharp=ImageEnhance.Sharpness(i)
new_sharp=5.32
i_sharp=cur_sharp.enhance(new_sharp)
i_sharp.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
