import pdf2image
import cv2
import numpy as np
from PIL import Image
import os
#################################            pdf to image             ###############################

before_pdf_path="before.pdf"
after_pdf_path="after.pdf"
images_after = pdf2image.convert_from_path(after_pdf_path) # add first pdf here
images_before = pdf2image.convert_from_path(before_pdf_path) # add ssecond pdf here
for i in range(len(images_after)):
    # Save pages as images in the pdf
    save_image_path="1"+str(i + 1) + ".jpg"
    images_after[i].save(save_image_path)
for i in range(len(images_before)):
    # Save pages as images in the pdf
    save_image_path= "2"+str(i + 1) + ".jpg"
    images_before[i].save(save_image_path)


no_of_pages_in_workbook2 = len(images_after)
no_of_pages_in_workbook1 = len(images_before)

#################################            image difference             ###########################

percent_diff = 0.0
# load images
for i in range(1, min(no_of_pages_in_workbook2, no_of_pages_in_workbook1) + 1):
    read_image_path="1" + str(i) + ".jpg"
    image1 = cv2.imread(read_image_path)
    read_image_path="2" + str(i) + ".jpg"
    image2 = cv2.imread(read_image_path)

    # compute difference
    difference = cv2.subtract(image1, image2)
    diff ="diff" + str(i) + ".png"
    cv2.imwrite(diff, difference)
    res = cv2.absdiff(image1, image2)

    # --- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(res) * 100) / res.size
    percent_diff = percent_diff + percentage

percent_diff = percent_diff / min(no_of_pages_in_workbook2, no_of_pages_in_workbook1)
text = str(round(percent_diff, 2)) + "% difference found"
print(text)


#############################            images to pdf               ##############################
lst = []
image_list = []
for i in range(1, min(no_of_pages_in_workbook2, no_of_pages_in_workbook1) + 1):
    temp ="diff" + str(i) + ".png"
    lst.append(Image.open(temp))
    if i != 1:
        image_list.append(lst[i - 1].convert("RGB"))
im_1 = lst[0].convert("RGB")
final_pdf_save_path="result.pdf"
im_1.save(final_pdf_save_path, save_all=True, append_images=image_list)
