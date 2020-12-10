import cv2

src=cv2.imread('test.jpg')
# 垂直翻转
img=cv2.flip(src,0)
# 写入文件
cv2.imwrite("test-rotated.jpg", img)
print('Successed.')
