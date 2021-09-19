import cv2
import numpy as np

def getdiff_img(source_path,target_path):
    source_file = source_path
    target_file = target_path
    kernel = np.ones((3, 3), np.uint8)

    n = np.fromfile(source_file, np.uint8)
    source_img = cv2.imdecode(n, cv2.IMREAD_COLOR)

    n = np.fromfile(target_file, np.uint8)
    target_img = cv2.imdecode(n, cv2.IMREAD_COLOR)

    if target_img is None:
        return 100000
    max_hight = max(source_img.shape[0], target_img.shape[0])
    max_width = max(source_img.shape[1], target_img.shape[1])

    temp_img = source_img
    source_img = np.zeros((max_hight, max_width, 3), dtype=np.uint8)
    source_img[0:temp_img.shape[0], 0:temp_img.shape[1]] = temp_img

    temp_img = target_img
    target_img = np.zeros((max_hight, max_width, 3), dtype=np.uint8)
    target_img[0:temp_img.shape[0], 0:temp_img.shape[1]] = temp_img

    result_img = cv2.addWeighted(source_img, 0.5, target_img, 0.5, 0)

    source_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
    img = cv2.absdiff(source_img, target_img)
    rtn, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    result_img = cv2.drawContours(result_img, contours, -1, (0, 0, 255))
    score = 0
    for contour in contours:
        score += cv2.contourArea(contour)
    score /= max_hight * max_width
    return score
