import cv2
import numpy as np

dir = "C:/users/berniehuang/downloads"

sentence = "你还记得它吗"
res = None

for c in sentence:
    fname = dir + "/" + c + ".jpg"
    img = cv2.imread(fname)

    if res is None:
        res = img
    else:
        res = np.hstack((res, img))


cv2.imwrite(dir + "/result.jpg", res)
