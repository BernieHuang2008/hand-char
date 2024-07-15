import cv2
import numpy as np

def transbg(fname):
    im = cv2.imread(fname+".jpg")

    # 二值化
    im = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY)[1]

    height, width, shape = im.shape
    new_im = np.ones((height, width, 4)) * 255
    new_im[:, :, :3] = im
    for i in range(height):
        for j in range(width):
            if new_im[i, j, :3].tolist() == [255.0, 255.0, 255.0]:
                new_im[i, j, :] = np.array([255.0, 255.0, 255.0, 0])
    cv2.imwrite(fname+".png", new_im)


if __name__ == "__main__":
    fprefix = "fontset2/src/S-"
    for i in range(1, 30):
        if i in [19]:
            continue
        print(i)
        fname = fprefix + str(i)
        transbg(fname)

