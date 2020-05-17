import cv2 as cv
import numpy as np

def get_image_info(image):
    # image是numpy数据类型，numpy怎么操作，image就怎么操作
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)

    pixel_data = np.array(image)
    print(pixel_data)

# 这个二值处理函数，对我来说就足够了
def global_threshold(image, image_name):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    high = gray.shape[0]
    weight = gray.shape[1]
    for cow in range(high):
        for col in range(weight):
            pv = gray[cow, col]
            if pv != 255:
                gray[cow, col] = 0
    cv.namedWindow(image_name, cv.WINDOW_NORMAL)
    cv.imshow(image_name, gray)

def process_case3():
    url = '/Users/allen/Desktop/map/'
    for i in range(10):
        img = cv.imread(url + str(i) + '.png')
        new_image = cv.resize(img,(200, 200))
        img_gray = cv.cvtColor(new_image, cv.COLOR_RGB2GRAY)

        h, w = img_gray.shape[:2]
        for row in range(h):
            for col in range(w):
                if img_gray[row, col] >20:
                    img_gray[row, col] = 255
                else:
                    img_gray[row,col] = 0
        pixel_data = np.array(img_gray)     # matrix类型
        np.savetxt(url+'csv/'+str(i)+'.csv', pixel_data, delimiter = ',')


if __name__ == '__main__':
    process_case3()
