import cv2
print("Enter file_name with extension in this folder(image):")
name = input()
print("Enter output file name without extension")
out = input()
out = out+".png"
image = cv2.imread(name)

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite(out, sketch) 
